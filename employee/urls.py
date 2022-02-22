from django.urls import include, path
from rest_framework import routers

from employee.views import PositionViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'positions', PositionViewSet, basename='positions')
router.register(r'employees', EmployeeViewSet, basename='employees')


urlpatterns = [
    path('', include(router.urls)),
]
