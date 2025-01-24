from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import (
    TeamForm,
    WorkerCreationForm,
    TaskForm,
    PositionNameSearchForm,
    TeamNameSearchForm,
    WorkerUsernameSearchForm,
    ProjectNameSearchForm,
    TaskTypeNameSearchForm,
    TaskNameSearchForm,
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

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PositionListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = PositionNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Position.objects.all()
        form = PositionNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("tasks:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:position-list")


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TeamListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TeamNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Team.objects.all()
        form = TeamNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasks:team-list")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("tasks:team-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("tasks:team-list")


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(WorkerListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Worker.objects.select_related("position", "team")
        form = WorkerUsernameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])

        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "position",
        "team",
    )
    success_url = reverse_lazy("tasks:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasks:worker-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(ProjectListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = ProjectNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Project.objects.prefetch_related("teams")
        form = ProjectNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("tasks:project-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("tasks:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("tasks:project-list")


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskTypeNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = TaskType.objects.all()
        form = TaskTypeNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "tasks/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = "tasks/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "tasks/task_type_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-type-list")
    context_object_name = "task_type"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "tasks/task_type_detail.html"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Task.objects.select_related("task_type", "project")
        form = TaskNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
