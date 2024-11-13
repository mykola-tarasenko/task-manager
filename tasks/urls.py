from .views import index, PositionListView, TeamListView

from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("teams/", TeamListView.as_view(), name="team-list"),
]

app_name = "tasks"
