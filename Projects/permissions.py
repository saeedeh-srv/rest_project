from rest_framework import permissions
from django.contrib.auth.models import User
from .models import Project, Task
from django.shortcuts import get_object_or_404


class CanUpdateDestroyProject(permissions.BasePermission):
    """
    custom permision to check if the user can update or delete project
    """

    def has_permission(self, request, view):
        user = request.user
        project_id = view.kwargs.get('pk')
        project = get_object_or_404(Project, id=project_id)

        try:
            if user == project.user:
                return True
        except user.DoesNotExist or project.DoesNotExist:
            pass
        return False


class CanUpdateDestroyTask(permissions.BasePermission):
    """
    Custom permission to check if the user can Update or Destroy a Task.
    """

    def has_permission(self, request, view):
        user = request.user
        task_id = view.kwargs.get('pk')
        task = get_object_or_404(Task, id=Task)
        if task:
            project = Project.objects.get(id=task.project.id)

        try:

            if user == project.user:
                return True
        except user.DoesNotExist or project.DoseNotExist:
            pass

        return False