# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('birth_date', models.DateField(blank=True)),
                ('sex', models.BooleanField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_time']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]
