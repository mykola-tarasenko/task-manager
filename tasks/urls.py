from django.urls import path

from .views import (
    index,
    PositionListView,
    PositionDetailView,
    TeamListView,
    TeamDetailView,
    WorkerListView,
    WorkerDetailView,
    ProjectListView,
    ProjectDetailView,
    TaskTypeListView,
    TaskListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>", PositionDetailView.as_view(), name="position-detail"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("teams/<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
]

app_name = "tasks"
