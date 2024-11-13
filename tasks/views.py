from django.shortcuts import render
from django.views import generic

from tasks.models import (
    Project,
    Team,
    Task,
    Position,
    Worker,
)


def index(request):
    """View function for the home page of the site."""

    num_projects = Project.objects.count()
    num_teams = Team.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_projects": num_projects,
        "num_teams": num_teams,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "tasks/index.html", context=context)


class PositionListView(generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "tasks/position_list.html"
    paginate_by = 5


class TeamListView(generic.ListView):
    model = Team
    context_object_name = "team_list"
    template_name = "tasks/team_list.html"
    paginate_by = 5


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "tasks/worker_list.html"
    paginate_by = 5
