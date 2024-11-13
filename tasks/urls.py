from .views import index, PositionListView

from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list")
]

app_name = "tasks"
