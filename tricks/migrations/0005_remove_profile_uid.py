# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0004_category_trick_tag_trick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='uid',
        ),
    ]
