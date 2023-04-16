from django.contrib import admin

from .models import Parents, Students, Courses, Schedules, Registrations

# Register your models here.
admin.site.register(Parents)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Schedules)
admin.site.register(Registrations)