from django.shortcuts import render, redirect
from django.http import request, JsonResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from .forms import SignupForm
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView


def home(request):
    return render(request, 'accounts/home.html', context = { 'user' : request.user })

# LOGIN VIEW
def login_view(request):
    if(request.user.is_anonymous):
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(to='accounts:profile')
            else:
                error_message = "Incorrect Username or Password"
                return render(request, 'accounts/login.html', {'error':error_message,'form':AuthenticationForm()})
        else:
            form = AuthenticationForm()
            return render(request, 'accounts/login.html', {'form':form})
    else:
        a = request.path
        print(a)
        if(request.path == "/accounts/login/"):
            return redirect(to='accounts:profile')
        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

# LOGOUT VIEW
@login_required
def logout_view(request):
    if(request.user.is_anonymous):
        return redirect(to='accounts:login')
    else:
        logout(request)
        return redirect(to='accounts:login')


def signup(request):
    if(request.user.is_anonymous):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect(to='accounts:profile')
            return render(request, 'accounts/signup.html', locals())
        else:
            form = SignupForm()
            return render(request, 'accounts/signup.html', context={'form':form})
    return redirect(to='accounts:profile')


@login_required(redirect_field_name='next', login_url='accounts:login')
def profile(request):
    return render(request, 'accounts/profile.html', context = {'user' :request.user})

@login_required(redirect_field_name='next', login_url='accounts:login')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has been changed successfully!", extra_tags='success-alert')
            return redirect(to='accounts:changepwd')
        return render(request, 'accounts/changePassword.html', locals())
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/changePassword.html', context = {'form':form})

class CustomPasswordReset(PasswordResetView, SuccessMessageMixin, FormView):
    template_name='accounts/password_reset_form.html'
    success_url=reverse_lazy('accounts:password_reset')
    success_message ="Email Sent"
    email_template_name='accounts/password_reset_email.html'
    subject_template_name='accounts/password_reset_subject.txt'

def resetPassword(request):
    if(request.user.is_anonymous):
        if request.method == 'POST':
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                form.save(request=request)
                messages.info(request, 'We\'ve emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly.If you don\'t receive an email, please make sure you\'ve entered the address you registered with, and check your spam folder.', extra_tags='info-alert')
                return redirect(to='accounts:resetpwd_done')
            return render(request, 'accounts/resetPassword.html', locals())
        else:
            form = PasswordResetForm()
            return render(request, 'accounts/resetPassword.html', context= {'form':form})
    else:
        return redirect(to='accounts:profile')
