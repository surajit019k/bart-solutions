from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'base.html')

def login(request):
    return render(request,'account/login.html')

def logout(request):
    return render(request,'account/logout.html')

def signup(request):
    return render(request,'account/signup.html')