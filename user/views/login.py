"""The View script for Login activities"""
from django import forms
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from user.models.logins import LoginModel
from django.contrib import messages

class LoginForm(forms.Form):
    email = forms.EmailField(label="Enter Email Address")
    password = forms.CharField(widget=forms.PasswordInput())

class LoginView(View):
    template_name = 'user/login.html'
    redirect = '/user/login'

    def get(self, request):
        return render(request,self.template_name,{'login_form':LoginForm})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.status is 0:
                #User account is not active
                messages.add_message(request, messages.ERROR, 'Your account is inactive, please contact the admin')
                return HttpResponseRedirect(self.redirect)
            else:
                login(request,user)
                #request.session['user_type'] = user.user_type
                return HttpResponseRedirect('/user/dashboard')
        else:
             messages.add_message(request, messages.ERROR, 'Invalid Email or Password!')
             return HttpResponseRedirect(self.redirect) 