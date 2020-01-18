from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm
# Create your views here.
#Return the index page
def index(request):
    return render(request, "index.html")

#User logout and redirect
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))

#Return the login page
def login(request):
    login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})