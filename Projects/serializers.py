from rest_framework import serializers
from .models import Project, Task, SubTask


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'pk',
            'title',
            'user',
            'description',
            'color',
            'image',
            'start_date',
            'end_date',
            'status',
            'budget',
            'content_id',

        )
        extra_kwargs = {
            'user': {'read_only': True},
        }


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'pk',
            'project',
            'title',
            'image',
            'color',
            'description',
            'budget',
            'start_date',
            'end_date',
            'status',
            'content_id',
        ]
        depth = 1
        extra_kwargs = {
            'project': {'read_only': True},
        }


class SubtaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = [
            'pk',
            'task',
            'title',
            'image',
            'color',
            'description',
            'budget',
            'start_date',
            'end_date',
            'status',
            'content_id',
        ]
        depth = 2
        extra_kwargs = {
            'task': {'read_only': True},
        }
