from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
#setup the index page
def index(request):
    return render(request, "index.html")

#setup the logout and redirect
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))

def login(request):
    return render(request, "login.html")