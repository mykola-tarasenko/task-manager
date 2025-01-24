from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Position

POSITION_URL = reverse("tasks:position-list")


class PublicPositionTest(TestCase):
    def test_login_required(self):
        res = self.client.get(POSITION_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatePositionTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_superuser(
            username="testuser",
            password="test1test23",
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(name="testposition1")
        Position.objects.create(name="testposition2")
        res = self.client.get(POSITION_URL)
        self.assertEqual(res.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(
            list(res.context["position_list"]),
            list(positions),
        )
        self.assertTemplateUsed(res, "tasks/position_list.html")


class PrivateWorkerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testadmin",
            password="test1test23",
        )
        self.client.force_login(self.user)

    def test_create_worker(self):
        form_data = {
            "username": "testuser",
            "password1": "test1test23",
            "password2": "test1test23",
            "first_name": "Test first",
            "last_name": "Test last",
        }
        self.client.post(reverse("tasks:worker-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.username, form_data["username"])
