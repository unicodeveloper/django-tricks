# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0003_auto_20150523_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Trick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='tricks.Category')),
                ('trick', models.ForeignKey(to='tricks.Trick')),
            ],
        ),
        migrations.CreateModel(
            name='Tag_Trick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.ForeignKey(to='tricks.Tag')),
                ('trick', models.ForeignKey(to='tricks.Trick')),
            ],
        ),
    ]
