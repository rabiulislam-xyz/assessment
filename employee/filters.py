import logging

from django_filters import filterset, CharFilter

from employee.models import Employee, Position


logger = logging.getLogger(__name__)


class EmployeeFilterSet(filterset.FilterSet):
    parent_position = CharFilter(method='parent_position_filter')

    class Meta:
        model = Employee
        fields = ['parent_position']

    # noinspection PyMethodMayBeStatic
    def parent_position_filter(self, queryset, name, value):
        if value:
            try:
                position = Position.objects.get(id=value)
                descendants = position.get_descendants()
                queryset = queryset.filter(position__in=descendants)
            except Position.DoesNotExist:
                logger.error('Position with id {} does not exist'.format(value))
                queryset = queryset.none()

        return queryset
