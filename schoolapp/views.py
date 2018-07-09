# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import    StudentSerializer,StudentFilterSerializer, AttendanceSerializer, TimeTableSerializer
from .models import StudentModel, TimetableModel, AttendanceModel
import requests
import json
from .tuk import SchoolSite

class StudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class classstudent:
    def student(self, name):
        print name

class StudentFilter(generics.RetrieveAPIView):
    serializer_class = StudentFilterSerializer
    # queryset = StudentModel.objects.all()



    model = StudentModel
    lookup_field = 'print_id'

    def get_object(self):
        student = self.request.query_params.get('print_id', None)
        query = self.model.objects.get(print_id=student)
        school = SchoolSite()
        reg = query.Reg_no
        print_id = query.print_id
        id = query.id
        school.feestatement(id,print_id,reg)

        return school.feestatement(id,print_id,reg)

#
#     def filter_queryset(self, queryset):
#         student = self.request.query_params.get('print_id', None)
#
#         if student is not None:
#             queryset = queryset.filter(print_id=student)
#             print queryset
#             return queryset

# class StudentFilter(generics.RetrieveUpdateAPIView):
#     queryset = StudentModel.objects.all()
#     lookup_field = 'print_id'
#
#     def get_serializer_class(self,):
#         if self.request.method == 'GET':
#             serializer_class = StudentFilterSerializer
#             return serializer_class
#         else:
#             serializer_class = StudentSerializer
#             return serializer_class

class TimeTableView(generics.ListCreateAPIView):
    serializer_class = TimeTableSerializer
    queryset = TimetableModel.objects.all()

class Attendanceview(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer
    queryset = AttendanceModel.objects.all()