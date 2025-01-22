from django.test import TestCase

from tasks.forms import WorkerCreationForm
from tasks.models import Position, Team


class FormsTests(TestCase):
    def test_worker_creation_form_with_first_last_name_is_valid(self):
        position = Position.objects.create(name="testposition")
        team = Team.objects.create(name="testteam")
        form_data = {
            "username": "testuser",
            "password1": "test1test23",
            "password2": "test1test23",
            "first_name": "Test first",
            "last_name": "Test last",
            "email": "ex12@mail.com",
            "position": position.pk,
            "team": team.pk,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], form_data["username"])
        self.assertEqual(form.cleaned_data["first_name"], form_data["first_name"])
        self.assertEqual(form.cleaned_data["last_name"], form_data["last_name"])
        self.assertEqual(form.cleaned_data["email"], form_data["email"])
        self.assertEqual(form.cleaned_data["position"], position)
        self.assertEqual(form.cleaned_data["team"], team)
