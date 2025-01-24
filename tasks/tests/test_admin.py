from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Position, Team


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="testadmin",
            password="test1test23",
        )
        self.client.force_login(self.admin_user)
        position = Position.objects.create(name="testposition")
        team = Team.objects.create(name="testteam")
        self.worker = get_user_model().objects.create_user(
            username="testuser",
            password="test1test23",
            position=position,
            team=team,
        )

    def test_worker_position_and_team_listed(self):
        """
        Test that worker's position and team are in list_display on worker admin page
        :return:
        """
        url = reverse("admin:tasks_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
        self.assertContains(res, self.worker.team)

    def test_worker_detail_position_and_team_listed(self):
        """
        Test that worker's position and team are on worker detail admin page
        :return:
        """
        url = reverse("admin:tasks_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
        self.assertContains(res, self.worker.team)
