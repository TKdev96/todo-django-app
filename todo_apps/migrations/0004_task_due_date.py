# Generated by Django 4.0.2 on 2022-03-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_apps', '0003_task_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
