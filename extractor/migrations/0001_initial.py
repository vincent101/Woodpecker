# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extractor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testPointFileName', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=10, choices=[(b'c2e', b'ChineseToEnglish'), (b'e2c', b'EnglishToChinese')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inputFileName', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=10, choices=[(b'c2e', b'ChineseToEnglish'), (b'e2c', b'EnglishToChinese')])),
                ('align', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('c', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('c_Berk', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('c_StanDep', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('c_StanTree', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('e', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('e_Berk', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('e_StanDep', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('e_StanTree', models.FileField(upload_to=b'./var/ExtractorInputFile/')),
                ('username', models.ManyToManyField(to='index.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='extractor',
            name='inputFileName',
            field=models.ForeignKey(to='extractor.Input'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extractor',
            name='username',
            field=models.ManyToManyField(to='index.User'),
            preserve_default=True,
        ),
    ]
