# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extractor',
            old_name='inputFileName',
            new_name='input',
        ),
        migrations.RemoveField(
            model_name='input',
            name='username',
        ),
    ]
