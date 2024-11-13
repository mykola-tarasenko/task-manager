from django.urls import path

from .views import (
    index,
    PositionListView,
    TeamListView,
    WorkerListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list")
]

app_name = "tasks"
