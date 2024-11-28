# Generated by Django 5.1.3 on 2024-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_project_teams"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
