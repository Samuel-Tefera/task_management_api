from rest_framework.viewsets import ModelViewSet, generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response

from task.serializers import TaskSerializer, TaskDetailSerializer, TaskStatisticSerializer
from core.models import Task

class TaskAPIViewSets(ModelViewSet):
    """API view for CRUD on Task"""
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        queryset = self.queryset

        # Filter by priority and status field
        priority = self.request.query_params.get('priority')
        status = self.request.query_params.get('status')

        if priority:
            queryset = queryset.filter(priority=priority)
        if status:
            queryset = queryset.filter(status=status)

        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskSerializer
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        partial = request.method == 'PATCH'
        instance = self.get_object()

        if 'is_completed' in request.data and request.data['is_completed'] == 'true':
            instance.mark_as_completed()
            return Response(self.get_serializer(instance).data)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


class TaskStatisticAPIView(generics.GenericAPIView):
    """API view for statistic on Tasks """
    serializer_class = TaskStatisticSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(status='COM').count()
        in_progress_tasks = tasks.filter(status='IP').count()
        pending_tasks = tasks.filter(status='PND').count()
        overdue_tasks = tasks.filter(status='OVD').count()
        completion_percentage = (completed_tasks / total_tasks) * 100
        completion_percentage_per_priority = {
            'high' :
                (tasks.filter(priority='HG', status='COM').count() / total_tasks) * 100,
            'medium' :
                (tasks.filter(priority='MD', status='COM').count() / total_tasks) * 100,
            'low' :
                (tasks.filter(priority='LW', status='COM').count() / total_tasks) * 100
        }

        data = {
            'total_tasks' : total_tasks,
            'completed_tasks' : completed_tasks,
            'in_progress_tasks' : in_progress_tasks,
            'pending_tasks' : pending_tasks,
            'overdue_tasks' : overdue_tasks,
            'completion_percentage' : completion_percentage,
            'completion_percentage_per_priority' : completion_percentage_per_priority,
        }

        return Response(data)