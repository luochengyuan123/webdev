# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person_nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u5bfc\u822a\u540d\u79f0')),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-date_publish'], 'verbose_name': '\u8bfe\u7a0b', 'verbose_name_plural': '\u8bfe\u7a0b'},
        ),
    ]
