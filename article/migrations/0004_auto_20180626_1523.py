# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment_article_id'),
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
