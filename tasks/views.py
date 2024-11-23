from django.shortcuts import render
from django.views import generic

from tasks.models import (
    Project,
    Team,
    Task,
    Position,
    Worker,
    TaskType,
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
    paginate_by = 5


class PositionDetailView(generic.DetailView):
    model = Position


class TeamListView(generic.ListView):
    model = Team
    paginate_by = 5


class TeamDetailView(generic.DetailView):
    model = Team


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Worker


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 5


class ProjectDetailView(generic.DetailView):
    model = Project


class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"
    paginate_by = 5


class TaskTypeDetailView(generic.DetailView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "tasks/task_type_detail.html"


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task
