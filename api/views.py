from typing import List
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from tasks.models import Tasks
from role.models import CustomUser
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from api.serializers import TaskSerializer, TaskAsignSerializer, TaskStatusSerializer
from rest_framework import permissions
from .permissions import IsClientOnly, IsEmployeeOnly, IsManagerOnly



class ViewAPIHome(APIView):
    """API Home"""
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        return Response({
            'Create Task': reverse_lazy('api:create', request=request),
            'Task List': reverse_lazy('api:list', request=request),
        })

class TaskCreateAPIView(CreateAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer
    permission_classes = [  permissions.IsAuthenticated, IsClientOnly,]


class TaskListAPIView(ListAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer
    permission_classes = [  permissions.IsAuthenticated, ]

    




class TaskDetailAPIView(RetrieveAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskAsignSerializer
    permission_classes = [  permissions.IsAuthenticated, IsManagerOnly,]

class TaskStatusUpdateAPIView(UpdateAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskStatusSerializer
    permission_classes = [  permissions.IsAuthenticated, IsEmployeeOnly,]



class TaskDestroyAPIView(DestroyAPIView):
    queryset=Tasks.objects.all()
    permission_classes = [  permissions.IsAuthenticated, IsManagerOnly,]



class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False