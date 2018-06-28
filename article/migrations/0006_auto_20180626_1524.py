# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
