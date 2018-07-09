# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    print_id = models.IntegerField()
    Reg_no = models.CharField(max_length=30)
    group = models.CharField(max_length=20)
    semester = models.CharField(max_length=1000, blank=True)
    course_name=models.CharField(max_length=1000, blank=True)
    course_code= models.CharField(max_length=1000, blank=True)
    bal=models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.Reg_no

class TimetableModel(models.Model):
    subject = models.CharField(max_length=2000)
    subject_code = models.CharField(max_length=10)
    day = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    semester = models.IntegerField()
    group = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.subject

class AttendanceModel(models.Model):
    student = models.ForeignKey(StudentModel, related_name='student', on_delete=models.CASCADE)
    subject = models.ForeignKey(TimetableModel, related_name='timetable', on_delete=models.CASCADE)
    time = models.TimeField(blank=True)