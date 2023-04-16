from django.db import models

# Create your enumarations here.
class Genders(models.TextChoices):
    MALE = 'M', ('Male')
    FEMALE = 'F', ('Female')

class Days(models.TextChoices):
    LUNES = 'Lun', ('Lunes')
    MARTES = 'Mar', ('Martes')
    MIERCOLES = 'Mie', ('Miércoles')
    JUEVES = 'Jue', ('Jueves')
    VIERNES = 'Vie', ('Viernes')
    SABADO = 'Sab', ('Sábado')
    DOMINGO = 'Dom', ('Domingo')

# Create your models here.
class Parents(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Genders.choices)
    birth_date = models.DateField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Students(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Genders.choices)
    birth_date = models.DateField()
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.ForeignKey(Parents, on_delete=models.CASCADE)

class Courses(models.Model):
    name = models.CharField(max_length=250)
    init_date = models.DateField()
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=200, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Schedules(models.Model):
    day = models.CharField(max_length=3, choices=Days.choices)
    init_hour = models.TimeField()
    end_hour = models.TimeField()
    link = models.URLField(null=True, max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)

class Registrations(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
