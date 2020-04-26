from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404, HttpResponseRedirect
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User, Org
from appeals.models import Appeal
from payments.models import Order
from taggit.models import Tag
from appeals.forms import AppealForm
from django.utils import timezone
from appeals.serializers import AppealsSerializer

@login_required
def create_appeal(request):
    """
    Ensures create appeal form is valid and pushes data into
    a new appeal, then redirects to appeals list page
    """
    if request.user.is_authenticated:
        active = "active"
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
            if request.method == "POST":
                form = AppealForm(request.POST)
                if form.is_valid():
                    appeal = form.save(commit=False)
                    appeal.author = request.user
                    appeal.org = Org.objects.get(user=request.user)
                    appeal.created_date = timezone.now()
                    appeal.save()
                    form.save_m2m()
                    messages.success(request, "Congratulations you have added an appeal")
                    return render(request, 'all_appeals.html', {'hasOrg': hasOrg, 'active6': active})
            else:
                form = AppealForm()
            return render(request, 'create_appeal.html', {'form': form,'hasOrg': hasOrg, 'active2': active})
        else:
            hasOrg = False
            messages.success(request, "You must create an organisation before setting up an appeal")
            return render(request, 'index.html', {'hasOrg': hasOrg, 'active1': active})
    else:
        return redirect(reverse('index'))

@login_required
def edit_appeal(request):
    """
    Ensures create appeal form is valid and pushes data into
    a new appeal, then redirects to appeals list page
    """
    if request.user.is_authenticated:
        owner = False
        previous = request.GET.get('next', '/')
        instance = get_object_or_404(Appeal, id=request.GET.get('id'))
        org = Org.objects.filter(user=request.user)
        form = AppealForm(request.POST or None, instance=instance)
        if request.method == "POST":
            if form.is_valid():
                appeal = form.save(commit=False)
                appeal.author = request.user
                appeal.org = Org.objects.get(user=request.user)
                appeal.created_date = timezone.now()
                appeal.save()
                form.save_m2m()
                messages.success(request, "Congratulations you have edited appeal called " + instance.title)
                return HttpResponseRedirect(previous)
            else:
                messages.error(request, "Unable to edit at this time.")
                return render(request, 'edit_appeal.html', {'form': form, 'previous': previous, 'instance': instance})
        else:
            return render(request, 'edit_appeal.html', {'form': form, 'previous': previous, 'instance': instance})
    else:
        active = "active"
        return render(request, 'index.html', {'active1': active})

def show_all_appeals(request):
    """
    Gets the appeals
    """
    all_appeals = Appeal.objects.filter(created_date__lte=timezone.now()).order_by('-money_target')
    active = "active"
    if request.user.is_authenticated:
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active}) 
        else:
            hasOrg = False
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active})
    else:
        hasOrg = False
        return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active})

@login_required
def single_appeal(request):
    """
    Gets the single appeal clicked on by a user
    """
    if request.user.is_authenticated:
        previous = request.GET.get('next', '/')
        owner = False
        org = Org.objects.filter(user=request.user)
        appeal = Appeal.objects.get(id=request.GET.get('id'))
        creator = appeal.author.id
        print(creator)
        if creator is request.user.id:
            owner = True
        orders = Order.objects.filter(appeal=appeal.id).order_by('-created_date')
        calcPercent = progress_perc(appeal.money_raised, appeal.money_target)
        if org:
            hasOrg = True
            return render(request, 'single_appeal.html', {'appeal': appeal, 'orders': orders, 'hasOrg': hasOrg, 'calcPercent': calcPercent, 'owner': owner, 'previous': previous}) 
        else:
            hasOrg = False
            return render(request, 'single_appeal.html', {'appeal': appeal, 'orders': orders,  'hasOrg': hasOrg, 'calcPercent': calcPercent, 'owner': owner, 'previous': previous}) 
    else:
        return redirect(reverse('index'))

def progress_perc(raised, target):
    """
    Calculates the percentage of the total
    """
    if raised is None:
        raised = 0    
    percentage = int((raised/target)*100)
    return percentage

class JSONResponse(HttpResponse):
    """
    returns the json object to the ajax call
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def all_appeal_map_data(request):
    """
    returns all the appeals data for maps api
    """
    if request.method == 'GET':
        all_appeals = Appeal.objects.all()
        serializer = AppealsSerializer(all_appeals, many=True)
        return JSONResponse(serializer.data)
