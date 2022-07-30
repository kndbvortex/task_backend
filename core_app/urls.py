from django.urls import path

from core_app import views


app_name = 'tasks'

urlpatterns = [
    path('', views.ListCreateTask.as_view(), name='list-create-task'),
    path('<int:task_id>/', views.RetrieveUpdateDeleteTaskView.as_view(), name='rud-task')
]

