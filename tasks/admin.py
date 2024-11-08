from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker, Project, Task, TaskType, Team, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "team",)
    list_filter = ["position", "team", ]
    search_fields = ["username", "first_name", "last_name", ]

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {
            "fields": ("position", "team",),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "position",
                "team",
            ),
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description", ]
    list_filter = ["teams", ]
    search_fields = ["name", ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "priority",
        "deadline",
        "project",
        "task_type",
        "description",
    ]
    list_filter = ["priority", "task_type", "project", "project__teams", ]
    search_fields = ["name", ]


admin.site.register(Position)
admin.site.register(Team)
admin.site.register(TaskType)
