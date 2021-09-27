from django_filters import rest_framework as filters
from django.db.models import Q

from .models import Task


class TaskFilter(filters.FilterSet):
    search = filters.CharFilter(field_name="text", lookup_expr='icontains')
    
    class Meta:
        model = Task
        fields = ['id']