from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from allauth.account.models import EmailAddress
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse
from mad_user.forms import *

# Create your views here.
def view_profile(request):
    try:
        profile=request.user.profile
    except:
        raise Http404()
    return render(request,'account/profile-view.html',{'profile':profile})

@login_required
def edit_profile(request):
    try:
        form=ProfileForm(instance=request.user.profile)
        if request.method == 'POST':
            form=ProfileForm(request.POST, request.FILES,instance=request.user.profile)
            if form.is_valid():
                form.save()

                if request.user.emailaddress_set.get(primary=True).verified:
                    return redirect('home')
                else:
                    return redirect('profile_verify_email')
            
        if request.path == reverse('profile-onboarding'):
            template='account/profile-onboarding.html'
        else:
            template='layouts/edit_layout.html'

        return render(request,template,{'form':form})
    except:
        raise Http404()

def delete_profile(request):
    user=request.user
    if request.method=='POST':
        logout(request)
        user.delete()
        return redirect('home')
    return render(request,'account/profile-delete.html')

def profile_verify_email(request):
    EmailAddress.objects.send_confirmation(request,request.user)