from .models import Project, Task, SubTask
from rest_framework import generics
from .permissions import permissions, CanUpdateDestroyProject, CanUpdateDestroyTask
from .serializers import ProjectSerializers, TaskSerializer, SubtaskSerializers
from django.shortcuts import get_object_or_404


class ProjectListCreateViews(generics.ListCreateAPIView):
    serializer_class = ProjectSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)


class ProjectListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializers
    permission_classes = [permissions.IsAuthenticated, CanUpdateDestroyProject]
    queryset = Project
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()

    def perform_destroy(self, instance):
        instance.delete()



class TaskProjectListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'pk'

    def get_queryset(self):
        tasks = Task.objects.filter(project_id=self.kwargs['pk'])
        return tasks

    def perform_create(self, serializer):
        pj = get_object_or_404(Project, id=self.kwargs['pk'])
        if serializer.is_valid():
            serializer.save(project=pj)


class TaskListUpdateDeleteViews(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, CanUpdateDestroyTask]
    queryset = Task
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            image = serializer.validated_data['image']
            if image is None:
                task = Task.objects.get(id=self.kwargs['pk'])
                print(task.image)
                serializer.save(image=task.image)
            serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class SubtaskListCreate(generics.ListCreateAPIView):
    serializer_class = SubtaskSerializers
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'pk'

    def get_queryset(self):
        tasks = SubTask.objects.filter(task_id=self.kwargs['pk'])
        return tasks

    def perform_create(self, serializer):
        task = get_object_or_404(Task, id=self.kwargs['pk'])
        if serializer.is_valid():
            serializer.save(task=task)

