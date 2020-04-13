from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from accounts.models import User, Org
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
                return render(request, 'index.html', {'hasOrg': hasOrg})
        else:
            form = AppealForm()
        return render(request, 'create_appeal.html', {'form': form,'hasOrg': hasOrg})
    else:
        hasOrg = False
        messages.success(request, "You must create an organisation before setting up an appeal")
        render(request, 'index.html', {'hasOrg': hasOrg})