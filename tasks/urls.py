from django.urls import path

from .views import (
    index,
    PositionListView,
    TeamListView,
    WorkerListView, ProjectListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("projects/", ProjectListView.as_view(), name="project-list"),
]

app_name = "tasks"
