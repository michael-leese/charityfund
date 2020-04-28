from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import Org
from accounts.forms import UserLoginForm, UserRegistrationForm, OrgRegistrationForm

#Return the index page
def index(request):
    """
    Returns the index page
    """
    active = "active"
    if request.user.is_authenticated:
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
        else:
            hasOrg = False
        return render(request, "index.html", {'hasOrg': hasOrg, 'active1': active})
    else:
        return render(request, "index.html", {'active1': active})

#User logout and redirect
@login_required
def logout(request):
    """
    Logout function
    """
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))

#Return the login page
def login(request):
    """
    Returns the login page
    """
    active = "active"
    previous = request.GET.get('next', '/')
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])        
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                if previous is None:
                    return redirect(reverse('index'))
                elif previous is not None:
                    return HttpResponseRedirect(previous)
            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
        return render(request, "login.html", {"login_form": login_form, 'active4': active})


#return the registration page
def register_user(request):
    """
    Register a user
    """
    active = "active"
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                hasOrg = False         
                return render(request, 'index.html', {"hasOrg": hasOrg, 'active1': active})
            else:
                messages.error(request, "Unable to register at this time.")
    else:
        register_form = UserRegistrationForm()
        return render(request, 'registration.html', {"register_form": register_form, 'active5': active})

#return the registration page
@login_required
def register_org(request):
    """
    Register an organisation
    """
    active = "active"
    if request.user.is_authenticated:
        if request.method == "POST":
            register_form = OrgRegistrationForm(request.POST, request.FILES)
            if register_form.is_valid():
                org = register_form.save(commit=False)
                org.user = request.user
                org.created_date = timezone.now()
                org.save()
                messages.success(request, "You have successfully registered an organisation")
                hasOrg = True
                return render(request, 'index.html', {'hasOrg': hasOrg, 'active1': active})
            else:
                messages.error(request, "Unable to register at this time.")
        else:
            register_form = OrgRegistrationForm()
            return render(request, 'organisation.html', {"register_form": register_form, 'active3': active})
    else:
        return redirect(reverse('index'))
        
def about(request):
    """
    Returns the about page to the user regardless of login status
    """
    active = "active"
    if request.user.is_authenticated:
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
            return render(request, 'about.html', {'hasOrg': hasOrg, 'active7': active}) 
        else:
            hasOrg = False
            return render(request, 'about.html', {'hasOrg': hasOrg, 'active7': active})
    else:
        hasOrg = False
        return render(request, 'about.html', {'hasOrg': hasOrg, 'active7': active})