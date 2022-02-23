from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from employee.filters import EmployeeFilterSet
from employee.models import Position, Employee
from employee.serializers import PositionSerializer, EmployeeSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', )


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all().order_by('position').select_related('position')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = EmployeeFilterSet
    search_fields = ('first_name', 'last_name')
