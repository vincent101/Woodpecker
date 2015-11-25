from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from index.models import User
from evaluation.models import Evaluation
import sqlite3

#class SelectForm(forms.Form):
    #checkbox = forms.BooleanField()

    #def __unicode__(self):
        #return checkbox

def showhistory(request):
    username = request.session.get('username','anybody')
    user = User.objects.get(username = username)
    entries_all = Evaluation.objects.filter(user = user)

    #cx = sqlite3.connect('db.sqlite3')
    #cu = cx.cursor()
    #cu.execute('select * from evaluation_evaluation where user')

    return render_to_response('history.html',{'entries_all':entries_all,'user':user})

def add(request):
    selectItem = request.GET['selectItem']
    print selectItem
    evaluations = Evaluation.objects.get(id = selectItem)
    print evaluations
    #return HttpResponse(evaluations)
    return render_to_response('history.html',{'evaluations':evaluations},context_instance=RequestContext(request))

def ajax_list(request):
    selectItem = request.GET['selectItem']
    print selectItem
    #evaluations = Evaluation.objects.get(id = selectItem)
    evaluations = range(100)
    print evaluations
    #return HttpResponse(json.dumps(evaluations),content_type='application/json')
    return HttpResponse(evaluations)

def ajax_dict(request):
    selectItem = request.GET['selectItem']
    print selectItem
    evaluations = Evaluation.objects.get(id = selectItem)
    print evaluations
    return HttpResponse(json.dumps(evaluations),content_type='application/json')
