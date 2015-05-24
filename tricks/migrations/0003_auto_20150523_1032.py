# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0002_auto_20150523_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='trick_id',
            new_name='trick',
        ),
    ]
