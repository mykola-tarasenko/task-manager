from django.shortcuts import render

from tasks.models import Project, Team, Task


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
