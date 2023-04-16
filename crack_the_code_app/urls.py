from rest_framework import routers

from .controllers import ParentsViewSet, StudentsViewSet, CoursesViewSet, SchedulesViewSet, RegistrationsViewSet

router = routers.DefaultRouter()

router.register('/parents', ParentsViewSet, 'parents')
router.register('/students', StudentsViewSet, 'students')
router.register('/courses', CoursesViewSet, 'courses')
router.register('/schedules', SchedulesViewSet, 'schedules')
router.register('/registrations', RegistrationsViewSet, 'registrations')

urlpatterns = router.urls
