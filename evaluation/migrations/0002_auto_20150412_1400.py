# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='username',
            new_name='user',
        ),
    ]
