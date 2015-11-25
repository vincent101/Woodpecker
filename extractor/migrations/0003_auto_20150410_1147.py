# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import extractor.models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0002_auto_20150410_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='align',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='c',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='c_Berk',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='c_StanDep',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='c_StanTree',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='e',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='e_Berk',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='e_StanDep',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='input',
            name='e_StanTree',
            field=models.FileField(upload_to=extractor.models.get_file_path),
            preserve_default=True,
        ),
    ]
