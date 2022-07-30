import django_filters.rest_framework
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from core_app.models import Task
from core_app.filter import TaskFilter
from core_app.serializer import TaskSerializer


class ListCreateTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    serializer_class = TaskSerializer
    filterset_class = TaskFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({"data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteTaskView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = "task_id"
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
