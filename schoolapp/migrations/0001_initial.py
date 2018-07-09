# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('print_id', models.IntegerField()),
                ('Reg_no', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=20)),
                ('semester', models.CharField(blank=True, max_length=1000)),
                ('course_name', models.CharField(blank=True, max_length=1000)),
                ('course_code', models.CharField(blank=True, max_length=1000)),
                ('bal', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TimetableModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=2000)),
                ('subject_code', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('group', models.CharField(max_length=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='attendancemodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='schoolapp.StudentModel'),
        ),
        migrations.AddField(
            model_name='attendancemodel',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable', to='schoolapp.TimetableModel'),
        ),
    ]
