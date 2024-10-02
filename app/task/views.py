from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response

from task.serializers import TaskSerializer, TaskDetailSerializer
from core.models import Task

class TaskAPIViewSets(ModelViewSet):
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
