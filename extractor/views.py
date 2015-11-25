from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext
from django import forms
from extractor.models import Extractor, Input

mode_choices = (
    ('c2e','ChineseToEnglish'),
    ('e2c','EnglishToChinese'),
    )

class ExtractForm(forms.Form):
    input = forms.ModelChoiceField(queryset=Input.objects.all())
    #inputFileName = forms.ModelChoiceField(queryset=Input.objects.raw('select inputFileName from extractor_input'))
    testPointFileName = forms.CharField(max_length=100)
    mode = forms.CharField(max_length=10, widget=forms.Select(choices=mode_choices))
    class Meta:
        model = Extractor

    def __unicede__(self):
        return self.testPointName

class InputForm(forms.Form):
    inputFileName = forms.CharField(max_length=100)
    mode = forms.CharField(max_length=10, widget=forms.Select(choices=mode_choices))
    align = forms.FileField()
    c = forms.FileField()
    c_Berk = forms.FileField()
    c_StanDep = forms.FileField()
    c_StanTree = forms.FileField()
    e = forms.FileField()
    e_Berk = forms.FileField()
    e_StanDep = forms.FileField()
    e_StanTree = forms.FileField()

    def __unicede__(self):
        return self.inputFileName

class DownlaodForm(forms.Form):
    input = forms.ModelChoiceField(queryset=Input.objects.all())

def extract(request):
    if request.method == "POST":
        ef = ExtractForm(request.POST, request.FILES)
        if ef.is_valid():
            testPointFileName = ef.cleaned_data['testPointFileName'] 
            input = ef.cleaned_data['input']
            mode = ef.cleaned_data['mode']
            testPointFileNames = Extractor.objects.filter(testPointFileName__exact = testPointFileName)
            if testPointFileNames :
                error = 'testPointFileName has been used.'
                return render_to_response('extractor.html',{'ef':ef,'error':error})
            else:
                extractorfiles = Extractor()
                extractorfiles.input = input
                extractorfiles.testPointFileName = testPointFileName
                #extractorfiles.username = username
                extractorfiles.mode = mode
                extractorfiles.save()
                error = 'successful.'
                print testPointFileName, mode
                return render_to_response('extractor.html',{'ef':ef,'error':error})
    else:
        ef = ExtractForm()
    return render_to_response('extractor.html',{'ef':ef})

def input(request):
    if request.method == "POST":
        uf = InputForm(request.POST, request.FILES)
        if uf.is_valid():
            inputFileName = uf.cleaned_data['inputFileName']
            #username = request.session.get('username','anybody')
            mode = uf.cleaned_data['mode']
            c = uf.cleaned_data['c']
            c_Berk = uf.cleaned_data['c_Berk']
            c_StanDep = uf.cleaned_data['c_StanDep']
            c_StanTree = uf.cleaned_data['c_StanTree']
            e = uf.cleaned_data['e']
            e_Berk = uf.cleaned_data['e_Berk']
            e_StanDep = uf.cleaned_data['e_StanDep']
            e_StanTree = uf.cleaned_data['e_StanTree']
            inputFileNames = Input.objects.filter(inputFileName__exact = inputFileName)
            if inputFileNames :
                error = 'inputFileName has been used.'
                return render_to_response('upload.html',{'uf':uf,'error':error})
            else:
                inputfiles = Input()
                inputfiles.inputFileName = inputFileName
                inputfiles.mode = mode
                inputfiles.c = c
                inputfiles.c_Berk = c_Berk
                inputfiles.c_StanDep = c_StanDep
                inputfiles.c_StanTree = c_StanTree
                inputfiles.e = e
                inputfiles.e_Berk = e_Berk
                inputfiles.e_StanDep = e_StanDep
                inputfiles.e_StanTree = e_StanTree
                inputfiles.save()
                error = 'successful.'
                print inputFileName, mode
                return render_to_response('upload.html',{'uf':uf,'error':error})
    else:
        uf = InputForm()
    return render_to_response('upload.html',{'uf':uf})

def download(request):
    if request.method == "POST":
        df = DownlaodForm(request.POST, request.FILES)
        if df.is_valid():
            input = uf.cleaned_data['input']

            with open(input) as f:
                c = f.read() 
            return HttpResponse(c)
    else:
        df = DownlaodForm()
    return render_to_response('download.html',{})

