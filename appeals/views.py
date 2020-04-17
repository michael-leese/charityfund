from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from accounts.models import User, Org
from appeals.models import Appeal
from taggit.models import Tag
from appeals.forms import AppealForm
from django.utils import timezone

# Create an appeal
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

def show_all_appeals(request):
    """
    Gets the appeals
    """
    active = "active"
    if request.user.is_authenticated:
        org = Org.objects.filter(user=request.user)
        all_appeals = Appeal.objects.filter(created_date__lte=timezone.now()).order_by('-money_target')
        if org:
            hasOrg = True
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active}) 
        else:
            hasOrg = False
            return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active})
    else:
        all_appeals = Appeal.objects.filter(created_date__lte=timezone.now()).order_by('-money_target')
        hasOrg = False
        return render(request, 'all_appeals.html', {'all_appeals': all_appeals, 'hasOrg': hasOrg, 'active6': active})

def single_appeal(request):
    """
    Gets the single appeal clicked on by a user
    """
    if request.user.is_authenticated:
        active = "active"
        org = Org.objects.filter(user=request.user)
        appeal = Appeal.objects.get(id=request.GET.get('id'))
        calcPercent = progress_perc(appeal.money_raised, appeal.money_target)
        if org:
            hasOrg = True
            return render(request, 'single_appeal.html', {'appeal': appeal, 'hasOrg': hasOrg, 'calcPercent': calcPercent}) 
        else:
            hasOrg = False
            return render(request, 'single_appeal.html', {'appeal': appeal, 'hasOrg': hasOrg, 'calcPercent': calcPercent}) 
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