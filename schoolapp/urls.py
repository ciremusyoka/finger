from django.conf.urls import url
from .views import StudentFilter,StudentView,Attendanceview, TimeTableView, attFilter

urlpatterns = [
    url(r'^students$', StudentView.as_view(), name='students'),
    url(r'^student/(?P<print_id>[0-9]+)$', StudentFilter.as_view(), name='edit-users'),
    url(r'^fees$', StudentFilter.as_view(), name='student_filter'),
    # url(r'^fees/(?P<print_id>[0-9]+)$', StudentFilter.as_view(), name='edit-student'),
    url(r'^timetable$', TimeTableView.as_view(), name='time_table'),
    url(r'^attendance$', Attendanceview.as_view(), name='attendance'),
    url(r'^att$', attFilter.as_view(), name='att'),
]