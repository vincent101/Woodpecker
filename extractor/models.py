from django.db import models
#from django.forms import ModelForm
from index.models import User


mode_choices = (
        ('c2e','ChineseToEnglish'),
        ('e2c','EnglishToChinese'),
        )

def get_file_path(instance, filename):
    paths = {'c2e':'c2e/','e2c':'e2c/'}
    return './var/ExtractorInputFile/'+paths[instance.mode]+instance.inputFileName+'/'+filename
    #return './var/ExtractorInputFile/'+paths[instance.mode]+filename

class Input(models.Model):
    inputFileName = models.CharField(max_length=100)
    #username = models.ManyToManyField(User)
    mode = models.CharField(max_length=10, choices=mode_choices)
    align = models.FileField(upload_to=get_file_path)
    c = models.FileField(upload_to=get_file_path)
    c_Berk = models.FileField(upload_to=get_file_path)
    c_StanDep = models.FileField(upload_to=get_file_path)
    c_StanTree = models.FileField(upload_to=get_file_path)
    e = models.FileField(upload_to=get_file_path)
    e_Berk = models.FileField(upload_to=get_file_path)
    e_StanDep = models.FileField(upload_to=get_file_path)
    e_StanTree = models.FileField(upload_to=get_file_path)

    def __unicode__(self):
        return self.inputFileName
        #return u'%d'%self.id

def get_file_path_forExtractor(instance, filename):
    paths = {'c2e':'c2e/','e2c':'e2c/'}
    return './var/DB_Checkpoint/'+paths[instance.mode]+instance.testPointFileName

class Extractor(models.Model):
    testPointFileName = models.CharField(max_length=100)
    input = models.ForeignKey(Input)
    username = models.ManyToManyField(User)
    mode = models.CharField(max_length=10, choices=mode_choices)
    testPointFile = models.FileField(upload_to=get_file_path_forExtractor)

    def __unicode__(self):
        return self.testPointFileName

#class InputForm(ModelForm):
    #class Meta:
        #model = Input
        #fields = ['inputFileName','username','mode']

#class ExtractorForm(ModelForm):
    #class Meta:
        #model = Extractor
        #fields = ['testPointFileName','username','mode']
