# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20180627_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]
