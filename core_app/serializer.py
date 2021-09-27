from rest_framework import serializers
from core_app.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True},
                        'day': {'input_formats': ['%d-%m-%Y', '%Y-%m-%d']},
                        		'output_format': ['%d-%m-%Y']}
