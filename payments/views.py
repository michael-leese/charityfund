from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from payments.forms import MakePaymentForm, OrderForm
from django.conf import settings
from django.utils import timezone
from appeals.models import Appeal
from accounts.models import User, Org
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required()
def make_payment(request):
    appeal = Appeal.objects.get(id=request.GET.get('id'))
    previous = request.GET.get('next', '/')
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            total = 0
            order = order_form.save(commit=False)
            total = order.amount
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                return HttpResponseRedirect(previous)
            
            if customer.paid:
                order.user = request.user
                order.appeal = Appeal.objects.get(id=request.GET.get('id'))
                order.org = Org.objects.get(id=appeal.org.id)
                order.created_date = timezone.now()
                order.successful = True
                order.save()
                appeal.money_raised += total
                appeal.save()
                messages.error(request, "Congratulations, you have successfully donated!")
                return HttpResponseRedirect(previous)
            else:
                order.user = request.user
                order.appeal = Appeal.objects.get(id=request.GET.get('id'))
                order.org = Org.objects.get(id=appeal.org.id)
                order.created_date = timezone.now()
                order.successful = False
                order.save()
                messages.error(request, "Unable to take payment")
                return render(request, "payment.html", {"appeal": appeal, "order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUB_KEY, "previous": previous})

        else:
            messages.error(request, "We were unable to take a payment with that card!")
            return render(request, "payment.html", {"appeal": appeal, "order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUB_KEY, "previous": previous})

    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        return render(request, "payment.html", {"appeal": appeal, "order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUB_KEY, "previous": previous})