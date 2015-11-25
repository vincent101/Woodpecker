from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from index.models import User

class UserForm_login(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm_register(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=100)

def register(request):
    if request.method == "POST":
        uf = UserForm_register(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password1 = uf.cleaned_data['password1']
            password2 = uf.cleaned_data['password2']
            email = uf.cleaned_data['email']
            if password1 == password2:
                users = User.objects.filter(username__exact = username)
                if users:
                    error = 'username has been used.'
                    return render_to_response('register.html',{'error':error, 'uf':uf})
                else:
                    User.objects.create(username = username, password = password1, email = email)
                    print username, password1
                    error = 'successful.'
                    return render_to_response('register.html',{'error':error, 'uf':uf})
            else:
                error = 'twice password is not same.'
                return render_to_response('register.html',{'error':error, 'uf':uf})
    else:
        uf = UserForm_register()
    return render_to_response('register.html',{'uf':uf})

def login(request):
    if request.method == "POST":
        uf = UserForm_login(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            users = User.objects.filter(username__exact = username, password__exact = password)
            if users:
                request.session['username'] = username
                print username, password
                return HttpResponseRedirect('/main/')
            else:
                error = 'username and password is not match.'
                return render_to_response('login.html',{'error':error,'uf':uf})
    else:
        uf = UserForm_login()
    return render_to_response('login.html',{'uf':uf})
