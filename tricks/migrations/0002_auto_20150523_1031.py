# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='trick',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='author',
            new_name='user',
        ),
    ]
