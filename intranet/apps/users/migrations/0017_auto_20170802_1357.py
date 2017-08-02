# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20170802_1355'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='email',
            unique_together=set([('user', 'address')]),
        ),
        migrations.AlterUniqueTogether(
            name='website',
            unique_together=set([('user', 'url')]),
        ),
    ]
