# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0007_auto_20150414_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='s_AdvTrans',
            new_name='S_AdvTrans',
        ),
    ]
