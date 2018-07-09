# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StudentModel, AttendanceModel, TimetableModel

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "print_id", "Reg_no"]

admin.site.register(StudentModel, StudentAdmin)


class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'subject_code', 'day', 'course', 'year', 'semester', 'group']

admin.site.register(TimetableModel, TimeTableAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'subject', 'time']

admin.site.register(AttendanceModel, AttendanceAdmin)