from rest_framework import viewsets, permissions

from .models import Parents, Students, Courses, Schedules, Registrations
from .serializers import ParentsSerializer, StudentsSerializer, CoursesSerializer, SchedulesSerializer, RegistrationsSerializer

# Create your controllers here.
class ParentsViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ParentsSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.method == 'GET':
            return Students.objects.all().select_related('parent_id')
        return Students.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = StudentsSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = CoursesSerializer

class SchedulesViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.method == 'GET':
            return Schedules.objects.all().select_related('course_id')
        return Schedules.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = SchedulesSerializer

class RegistrationsViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.request.method == 'GET':
            return Registrations.objects.all().select_related('course_id', 'student_id')
        return Registrations.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = RegistrationsSerializer
