# Generated by Django 3.2 on 2021-04-26 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='todo name')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End date')),
                ('description', models.TextField(max_length=2000, null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='todo name')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End date')),
                ('description', models.TextField(max_length=2000, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.task')),
            ],
        ),
    ]