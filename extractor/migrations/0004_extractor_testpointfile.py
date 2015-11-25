# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import extractor.models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0003_auto_20150410_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='extractor',
            name='testPointFile',
            field=models.FileField(default='./var/DB_Checkpoint/', upload_to=extractor.models.get_file_path_forExtractor),
            preserve_default=False,
        ),
    ]
