from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="workers"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="members"
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"@{self.username}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teams = models.ManyToManyField(Team, blank=True, related_name="projects")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField(
        choices=[
            (1, "Urgent"),
            (2, "High"),
            (3, "Medium"),
            (4, "Low"),
        ],
        default=4,
    )
    status = models.IntegerField(
        choices=[
        (1, "Pending"),
        (2, "In progress"),
        (3, "Completed"),
        ],
        default=1,
    )
    deadline = models.DateField(null=True, blank=True)
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("name", "priority", "status", "deadline", "task_type", "project",)

    def __str__(self):
        return self.name
