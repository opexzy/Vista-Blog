"""The View script for Login activities"""
from django import forms
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from user.models import LoginModel

CHOICES = [('M', 'Male'), ('F', 'Female')]
class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name: ")
    last_name = forms.CharField(label="Last Name: ")
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
    retype_password = forms.CharField(label="Retype Password",widget=forms.PasswordInput())
    gender = forms.ChoiceField(label="Gender", choices=CHOICES)

class RegisterView(View):
    template_name = 'user/register.html'

    def get(self, request):
        return render(request,self.template_name,{'register_form':RegisterForm})

    def post(self, request):
        redirect = '/user/register'
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            #check if password are the the same
            if data.get('password') != data.get('retype_password'):
                # create flash message and redirect
                messages.add_message(request, messages.ERROR, 'Password do not match!')
                return HttpResponseRedirect(redirect)

            #Add new user to database and check for errors
            run_process =  LoginModel.manage.add_new_user(data.get('email'), data.get('password'), first_name=data.get('first_name'),
            last_name=data.get('last_name'), gender=data.get('gender'))
            if run_process:
                messages.add_message(request, messages.SUCCESS, 'Registration was successful')
                return HttpResponseRedirect(redirect)
            else:
                messages.add_message(request, messages.ERROR, 'An account with this email already exist, try using a different email')
                return HttpResponseRedirect(redirect)
        else:
            messages.add_message(request, messages.WARNING, 'We detected some errors in your details !')
            return HttpResponseRedirect(redirect)

