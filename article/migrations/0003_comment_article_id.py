# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article_id',
            field=models.ForeignKey(to='article.Article', default=-1),
            preserve_default=False,
        ),
    ]
