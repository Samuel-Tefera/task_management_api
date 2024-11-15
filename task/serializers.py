from rest_framework import serializers

from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task Model."""
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
                'id', 'title', 'category', 'status', 'priority',
                'created_at', 'due_date', 'completed_at', 'duration'
            ]

    def get_duration(self, obj):
        return f'{obj.duration()} days' if obj.duration() else 'Task not completed yet!'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def updatte(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class TaskDetailSerializer(TaskSerializer):
    """Serializer for Task detail view. """
    class Meta:
        model = Task
        fields = TaskSerializer.Meta.fields + ['description']


class TaskStatisticSerializer(serializers.Serializer):
    """Serailizer for Task Statistic."""
    total_tasks = serializers.IntegerField()
    completed_tasks = serializers.IntegerField()
    in_progress_tasks = serializers.IntegerField()
    pending_tasks = serializers.IntegerField()
    overdue_tasks = serializers.IntegerField()
    completion_percentage = serializers.FloatField()
    completion_percentage_per_priority = serializers.DictField()
