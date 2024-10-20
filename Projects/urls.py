from django.urls import path
from .views import ProjectListCreateViews, ProjectListUpdateDeleteView, \
    TaskProjectListCreate, SubtaskListCreate, TaskListUpdateDeleteViews

app_name = 'projects'

urlpatterns = [
    path('list/create/', ProjectListCreateViews.as_view(), name='project_list_create'),
    path('update/destroy/<int:pk>/', ProjectListUpdateDeleteView.as_view(), name='project_list_update_delete'),
path('task/<int:pk>/', TaskProjectListCreate.as_view(), name='create_list_task_project'),
    path('task/update/destroy/<int:pk>/', TaskListUpdateDeleteViews.as_view(),
         name='update_destroy_project'),
    path('subtask/<int:pk>/', SubtaskListCreate.as_view(), name='create_list_subtask_task_project'),
]
