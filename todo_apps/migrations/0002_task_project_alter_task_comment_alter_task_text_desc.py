# Generated by Django 4.0.2 on 2022-03-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ManyToManyField(to='todo_apps.Project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='text_desc',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
