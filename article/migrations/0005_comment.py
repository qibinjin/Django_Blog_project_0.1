# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180626_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('author', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('article_id', models.ForeignKey(to='article.Article')),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
