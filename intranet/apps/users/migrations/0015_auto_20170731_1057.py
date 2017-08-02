# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 14:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import intranet.apps.preferences.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20161017_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('h', 'Home Phone'), ('m', 'Mobile Phone'), ('o', 'Other Phone')], default='o', max_length=1)),
                ('number', intranet.apps.preferences.fields.PhoneField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_number', models.IntegerField(choices=[(9, 'Freshman'), (10, 'Sophomore'), (11, 'Junior'), (12, 'Senior'), (13, 'Staff')])),
                ('binary', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='cache',
        ),
        migrations.AddField(
            model_name='user',
            name='admin_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='counselor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='user',
            name='grade_number',
            field=models.IntegerField(choices=[(9, 'Freshman'), (10, 'Sophomore'), (11, 'Junior'), (12, 'Senior'), (13, 'Staff')], default=9),
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='parent_show_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='parent_show_birthday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='parent_show_eighth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='parent_show_pictures',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='parent_show_telephone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='self_show_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='self_show_birthday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='self_show_eighth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='self_show_pictures',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='self_show_telephone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.CharField(max_length=7, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('counselor', 'Counselor'), ('user', 'Attendance-Only User'), ('simple_user', 'Simple User'), ('tjstar_presenter', 'tjStar Presenter')], default='student', max_length=30),
        ),
        migrations.DeleteModel(
            name='UserCache',
        ),
        migrations.AddField(
            model_name='website',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='websites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='email',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.Photo'),
        ),
    ]
