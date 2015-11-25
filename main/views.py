from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from index.models import User

def main(request):
    return render_to_response('main.html',{})

def left(request):
    return render_to_response('left.html',{})

def welcome(request):
    username = request.session.get('username','anybody')
    return render_to_response('welcome.html',{'username':username})
