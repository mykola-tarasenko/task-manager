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
        queryset=get_user_model().objects.filter(team__isnull=True),
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

    def save(self, commit=True):
        team = super().save(commit=False)
        if commit:
            team.save()
        if "workers" in self.cleaned_data:
            workers = self.cleaned_data["workers"]
            for worker in workers:
                worker.team = team
                worker.save()
        if "projects" in self.cleaned_data:
            projects = self.cleaned_data["projects"]
            for project in projects:
                project.teams.add(team)
        return team


class WorkerCreationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("position", "team",)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < datetime.date.today():
            raise forms.ValidationError("The deadline cannot be in the past.")
        return deadline