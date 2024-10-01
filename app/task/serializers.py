from rest_framework import serializers

from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task Model."""
    class Meta:
        model = Task
        fields = ['id', 'title', 'category', 'status', 'priority', 'created_at', 'due_date']

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def updatte(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class TaskDetailSerializer(TaskSerializer):
    """Serializer doe Task detail view. """
    class Meta:
        model = Task
        fields = TaskSerializer.Meta.fields + ['description', 'completed_at']
