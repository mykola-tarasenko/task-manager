from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import (
    TeamForm,
    WorkerCreationForm,
    TaskForm,
)
from tasks.models import (
    Project,
    Team,
    Task,
    Position,
    Worker,
    TaskType,
)


@login_required
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


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 5


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasks:team-list")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasks:team-list")


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 5


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("tasks:project-list")


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"
    paginate_by = 5


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "tasks/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "tasks/task_type_detail.html"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
