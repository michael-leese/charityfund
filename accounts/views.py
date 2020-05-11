from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import Org, UserProfile
from appeals.models import Appeal
from payments.models import Order
from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, OrgRegistrationForm

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
        userprofile = UserProfile.objects.get(user=request.user)
        return render(request, "index.html", {'hasOrg': hasOrg, 'active1': active, 'userprofile': userprofile})
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
                return render(request, "login.html", {"login_form": login_form, 'active4': active})
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
        profile_form = UserProfileForm(request.POST, request.FILES)     
        if register_form.is_valid() and profile_form.is_valid():
            register_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            hasOrg = False
            if user:
                myuserprofile = profile_form.save(commit=False)
                myuserprofile.user = user
                myuserprofile.save()
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                userprofile = UserProfile.objects.get(user=user)
                return render(request, 'index.html', {"hasOrg": hasOrg, 'active1': active, 'userprofile': userprofile})
            else:
                messages.error(request, "Unable to register at this time.")
                return render(request, 'registration.html', {"register_form": register_form, 'profile_form': profile_form, 'active5': active})
        else:
            return render(request, 'registration.html', {"register_form": register_form, 'profile_form': profile_form, 'active5': active})
    else:
        register_form = UserRegistrationForm()
        profile_form = UserProfileForm()
        return render(request, 'registration.html', {"register_form": register_form, 'profile_form': profile_form, 'active5': active})

#return the registration page
@login_required
def register_org(request):
    """
    Register an organisation
    """
    active = "active"
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(user=request.user)
        if request.method == "POST":
            register_form = OrgRegistrationForm(request.POST, request.FILES)
            if register_form.is_valid():
                org = register_form.save(commit=False)
                org.user = request.user
                org.created_date = timezone.now()
                org.save()
                messages.success(request, "You have successfully registered an organisation")
                hasOrg = True
                return render(request, 'index.html', {'hasOrg': hasOrg, 'active1': active, 'userprofile': userprofile})
            else:
                messages.error(request, "Unable to register at this time.")
                return render(request, 'organisation.html', {"register_form": register_form, 'active3': active, 'userprofile': userprofile})
        else:
            register_form = OrgRegistrationForm()
            return render(request, 'organisation.html', {"register_form": register_form, 'active3': active, 'userprofile': userprofile})
    else:
        return redirect(reverse('index'))
        
def about(request):
    """
    Returns the about page to the user regardless of login status
    """
    active = "active"
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(user=request.user)
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
            return render(request, 'about.html', {'hasOrg': hasOrg, 'active7': active, 'userprofile': userprofile}) 
        else:
            hasOrg = False
            return render(request, 'about.html', {'hasOrg': hasOrg, 'active7': active, 'userprofile': userprofile})
    else:
        hasOrg = False
        return render(request, 'about.html', {'hasOrg': hasOrg, 'active7': active})

@login_required
def edit_org(request):
    """
    Edit the organisation that belongs to the user if any
    """
    active = "active"
    if request.user.is_authenticated:
        hasOrg = True
        instance = get_object_or_404(Org, user=request.user)
        org = Org.objects.filter(user=request.user)
        userprofile = UserProfile.objects.get(user=request.user)
        if request.method == "POST":
            form = OrgRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                org = form.save(commit=False)
                if org.image != instance.image:
                    instance.image.delete(save=True)
                org.image = request.FILES["image"]
                org.user = request.user
                org.id = instance.id
                org.save(force_update=True)
                messages.success(request, "Congratulations you have edited organisation called " + instance.organisation)
                return render(request, 'index.html', {'active1': active, 'userprofile': userprofile, 'hasOrg': hasOrg})
            else:
                messages.error(request, "Unable to edit at this time.")
                return render(request, 'editorg.html', {'form': form, 'instance': instance, 'userprofile': userprofile, 'active9': active, 'hasOrg': hasOrg})
        else:
            form = OrgRegistrationForm(instance=instance)
            return render(request, 'editorg.html', {'form': form, 'instance': instance, 'userprofile': userprofile, 'active9': active, 'hasOrg': hasOrg})
    else:
        return render(request, 'index.html', {'active1': active})

def view_my_orgs_appeals(request):
    """
    Get the org and appeals for the user
    """
    filterType = request.GET.get('filter')
    if filterType is None:
        filterType = '-created_date'
    orders = Order.objects.filter(user=request.user).order_by('-created_date')[:5] 
    active = "active"
    if request.user.is_authenticated:
        logged_in = True
        userprofile = UserProfile.objects.get(user=request.user)
        all_appeals = Appeal.objects.filter(author=request.user).order_by(filterType)
        org = Org.objects.get(user=request.user)
        if org:
            hasOrg = True
            return render(request, 'all_orgs_appeals.html', {'all_appeals': all_appeals, 'orders': orders, 'hasOrg': hasOrg, 
                                                        'active9': active, 'logged_in': logged_in, 'userprofile': userprofile, 'org': org}) 
        else:
            hasOrg = False
            return render(request, 'index.html', {'hasOrg': hasOrg, 'active1': active, 'userprofile': userprofile})
    else:
        return render(request, 'index.html', {'active1': active})

@login_required
def change_password(request):
    '''
    Change the users password.
    '''
    active = "active"
    org = False
    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(user=request.user)
        org = Org.objects.filter(user=request.user)
        if org:
            hasOrg = True
        if request.method == "POST":
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "You have successfully changed your password.")
                return render(request, 'edituserprofile.html', {"hasOrg": hasOrg, 'active1': active, 'userprofile': userprofile})
            else:
                messages.error(request, "Unable to change password at this time.")
                return render(request, 'changepassword.html', {"password_form": password_form, 'userprofile': userprofile})
        else:
            password_form = PasswordChangeForm(request.user)
            return render(request, 'changepassword.html', {"password_form": password_form, 'userprofile': userprofile})
    else:
        return render(request, 'index.html', {'active1': active})

@login_required
def edit_user_profile(request):
    '''
    Edit users profile
    '''
    active = "active"
    if request.user.is_authenticated:
        hasOrg = False
        instance = get_object_or_404(UserProfile, user=request.user)
        org = Org.objects.filter(user=request.user)
        if request.method == "POST":
            profile_form = UserProfileForm(request.POST, request.FILES)
            if profile_form.is_valid():
                user_profile = profile_form.save(commit=False)
                if user_profile.profile_picture != instance.profile_picture:
                    instance.profile_picture.delete(save=True)
                user_profile.profile_picture = request.FILES["profile_picture"]
                user_profile.user = request.user
                user_profile.id = instance.id
                user_profile.save(force_update=True)
                messages.success(request, "You have successfully updated your user profile")
                return render(request, 'index.html', {'active1': active, 'userprofile': user_profile, 'hasOrg': hasOrg})
            else:
                messages.error(request, "Unable to edit at this time.")
                return render(request, 'edituserprofile.html', {'profile_form': profile_form, 'userprofile': instance, 'active10': active, 'hasOrg': hasOrg})
        else:
            profile_form = UserProfileForm(instance=instance)
            return render(request, 'edituserprofile.html', {'profile_form': profile_form, 'userprofile': instance, 'active10': active, 'hasOrg': hasOrg})
    else:
        return render(request, 'index.html', {'active1': active})