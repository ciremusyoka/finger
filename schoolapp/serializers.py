from rest_framework import serializers
from .models import StudentModel, TimetableModel, AttendanceModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('__all__')

class StudentFilterSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=1000)
    cl = serializers.CharField(max_length=5)
    class Meta:
        model = StudentModel
        fields = ('id', 'name', 'print_id', 'Reg_no', 'semester', 'course_name', 'course_code', 'bal', 'message', 'cl')

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableModel
        fields = ('__all__')

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModel
        fields = ('__all__')