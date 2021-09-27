from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import generics

from core_app.models import Task
from core_app.filter import TaskFilter
from core_app.serializer import TaskSerializer

class ListCreateTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class RetrieveUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "task_id"
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
