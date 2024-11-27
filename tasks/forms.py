from django import forms
from django.contrib.auth import get_user_model

from tasks.models import Team, Project


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
        fields = ('name',)

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
