from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from accounts.models import User, Org
from appeals.models import Appeal
from appeals.forms import AppealForm
from django.utils import timezone

# Create an appeal
def create_appeal(request):
    """
    Ensures create appeal form is valid and pushes data into
    a new appeal, then redirects to appeals list page
    """
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
                messages.success(request, "Congratulations you have added an appeal")
                return render(request, 'all_appeals.html', {'hasOrg': hasOrg})
        else:
            form = AppealForm()
        return render(request, 'create_appeal.html', {'form': form,'hasOrg': hasOrg})
    else:
        hasOrg = False
        messages.success(request, "You must create an organisation before setting up an appeal")
        return render(request, 'index.html', {'hasOrg': hasOrg})

def show_all_appeals(request):
    """
    Gets the appeals
    """
    if request.user.is_authenticated:
        org = Org.objects.filter(user=request.user)
        all_appeals = Appeal.objects.filter(created_date__lte=timezone.now()).order_by('-money_target')
        if org:
            hasOrg = True
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg}) 
        else:
            hasOrg = False
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg})
    else:
        all_appeals = Appeal.objects.filter(created_date__lte=timezone.now()).order_by('-money_target')
        hasOrg = False
        return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg})

def single_appeal(request):
    """
    Gets the single appeal
    """
    org = Org.objects.filter(user=request.user)
    all_appeals = Appeal.objects.filter(created_date__lte=timezone.now()).order_by('-money_target')
    if org:
        hasOrg = True
        return render(request, 'index.html', {'hasOrg': hasOrg}) 
    else:
        hasOrg = False
        return render(request, 'index.html', {'hasOrg': hasOrg}) 