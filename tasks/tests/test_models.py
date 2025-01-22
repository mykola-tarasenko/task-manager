from django.test import TestCase

from tasks.models import (
    Position,
    Worker,
    Project,
    TaskType,
    Task,
    Team,
)


class ModelsTest(TestCase):
    def test_position_str(self):
        position = Position.objects.create(name="testposition")
        self.assertEqual(str(position), position.name)

    def test_team_str(self):
        team = Team.objects.create(name="testteam")
        self.assertEqual(str(team), team.name)

    def test_worker_str(self):
        worker = Worker.objects.create_user(
            username="testuser",
            password="test1test23",
        )
        self.assertEqual(str(worker), f"@{worker.username}")

    def test_project_str(self):
        project = Project.objects.create(name="testproject")
        self.assertEqual(str(project), project.name)

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="testtasktype")
        self.assertEqual(str(task_type), task_type.name)

    def test_task_str(self):
        task_type = TaskType.objects.create(name="testtasktype")
        project = Project.objects.create(name="testproject")
        task = Task.objects.create(
            name="testtask",
            task_type=task_type,
            project=project,
        )
        self.assertEqual(str(task), task.name)

    def test_create_worker(self):
        username = "testuser"
        password = "test1test23"
        position = Position.objects.create(name="testposition")
        team = Team.objects.create(name="testteam")
        worker = Worker.objects.create_user(
            username=username,
            password=password,
            position=position,
            team=team,
        )
        self.assertEqual(worker.username, username)
        self.assertEqual(worker.position, position)
        self.assertEqual(worker.team, team)
        self.assertTrue(worker.check_password(password))
