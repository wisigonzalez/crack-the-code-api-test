from rest_framework import serializers

from .models import Parents, Students, Courses, Schedules, Registrations

class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ('id', 'name', 'last_name', 'gender', 'birth_date', 'email', 'created_at', 'updated_at')

class StudentsSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent_id.name', read_only=True)
    parent_last_name = serializers.CharField(source='parent_id.last_name', read_only=True)

    class Meta:
        model = Students
        fields = ('id', 'name', 'last_name', 'gender', 'birth_date', 'email', 'created_at', 'updated_at', 'parent_id', 'parent_name', 'parent_last_name')
    
    def to_representation(self, instance):
        # Obtener el valor del método HTTP utilizado
        http_method = self.context.get('request').method
        if http_method == 'GET':
            # Si el método es GET, incluir la información del padre
            return super().to_representation(instance)
        else:
            # Si no es GET, excluir la información del padre
            data = super().to_representation(instance)
            data.pop('parent', None)
            return data

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'name', 'init_date', 'duration', 'price', 'created_at', 'updated_at')

class SchedulesSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course_id.name', read_only=True)
    course_init_date = serializers.DateField(source='course_id.last_name', read_only=True)

    class Meta:
        model = Schedules
        fields = ('id', 'day', 'init_hour', 'end_hour', 'link', 'created_at', 'updated_at', 'course_id', 'course_name', 'course_init_date')
    
    def to_representation(self, instance):
        # Obtener el valor del método HTTP utilizado
        http_method = self.context.get('request').method
        if http_method == 'GET':
            # Si el método es GET, incluir la información del padre
            return super().to_representation(instance)
        else:
            # Si no es GET, excluir la información del padre
            data = super().to_representation(instance)
            data.pop('course', None)
            return data

class RegistrationsSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course_id.name', read_only=True)
    course_init_date = serializers.DateField(source='course_id.last_name', read_only=True)

    student_name = serializers.CharField(source='student_id.name', read_only=True)
    student_last_name = serializers.CharField(source='student_id.last_name', read_only=True)

    class Meta:
        model = Registrations
        fields = ('id', 'created_at', 'updated_at', 'course_id', 'student_id', 'course_name', 'course_init_date', 'student_name', 'student_last_name')
