# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20180626_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
