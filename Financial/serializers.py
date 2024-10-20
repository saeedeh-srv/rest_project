from abc import ABC
from rest_framework import serializers
from .models import FinancialRecord,FinancialProjectInput
from Projects.models import Project, Task, SubTask
from Projects.serializers import ProjectSerializers, \
    TaskSerializer, SubtaskSerializers


class FinancialRecordRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        if isinstance(value, Project):
            serializer = ProjectSerializers(value)
        elif isinstance(value, Task):
            serializer = TaskSerializer(value)
        elif isinstance(value, SubTask):
            serializer = SubtaskSerializers(value)
        else:
            raise serializers.ValidationError({"Exception": "unexpected type of object"})
        return serializer.data


class FinancialRecordSerializers(serializers.ModelSerializer):
    content_object = FinancialRecordRelatedField(read_only=True)

    class Meta:
        model = FinancialRecord
        fields = [
            'pk',
            'who_created',
            'title',
            'price',
            'description',
            'create',
            'update',
            'status',
            'content_type',
            'object_id',
            'content_object',
        ]
        extra_kwargs = {
            'who_created': {'read_only': True}
        }


class FinancialProjectInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialProjectInput
        fields = [
            'pk',
            'who_created',
            'project',
            'financial_record',
            'expense_type',
            'description',
            'amount',
            'date',
        ]

    extra_kwargs = {
        'who_created': {'read_only': True},
        'project': {'read_only': True},
        'financial_record': {'read_only': True},
    }