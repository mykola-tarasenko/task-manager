import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from tasks.models import (
    Team,
    Project,
    Worker,
    Task,
)


class TeamForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    projects = forms.ModelMultipleChoiceField(
        queryset=Project.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Team
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        team_instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        if team_instance:
            self.fields["workers"].initial = team_instance.members.all()
            self.fields["projects"].initial = team_instance.projects.all()

    def save(self, commit=True):
        team = super().save(commit=False)
        if commit:
            team.save()
        if "workers" in self.cleaned_data:
            workers = self.cleaned_data["workers"]
            previous_workers = set(team.members.all())
            current_workers = set(workers)
            removed_workers = previous_workers - current_workers
            for worker in removed_workers:
                worker.team = None
                worker.save()

            for worker in current_workers:
                worker.team = team
                worker.save()

        if "projects" in self.cleaned_data:
            projects = self.cleaned_data["projects"]
            team.projects.clear()
            for project in projects:
                project.teams.add(team)
        return team


class WorkerCreationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("position", "team", "first_name", "last_name", "email")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        status = self.cleaned_data.get("status")
        if deadline and deadline < datetime.date.today() and status < 3:
            raise forms.ValidationError("The deadline cannot be in the past.")
        return deadline
