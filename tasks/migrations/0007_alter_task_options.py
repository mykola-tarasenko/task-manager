# Generated by Django 5.1.3 on 2024-11-28 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0006_alter_task_priority_alter_task_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("name", "priority", "status")},
        ),
    ]
