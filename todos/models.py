import traceback

from django.db import models

# Create your models here.
from accounts.models import Users


class Task(models.Model):
    name = models.CharField(verbose_name="todo name", max_length=500, null=False, blank=False)
    start_date = models.CharField(verbose_name='Start date', null=True, blank=True,max_length=500)
    end_date = models.CharField(verbose_name='End date', null=True, blank=True,max_length=500)
    description = models.TextField(max_length=2000, null=True)
    deleted = models.BooleanField(default=False)


    @staticmethod
    def all_tasks():
        return Task.objects.filter(deleted=False);


class Todo(models.Model):
    name = models.CharField(verbose_name="todo name",max_length=500, null=False,blank=False)
    start_date= models.CharField(verbose_name='Start date', null=True, blank=True,max_length=500)
    end_date = models.CharField(verbose_name='End date', null=True, blank=True,max_length=500)
    description = models.TextField(max_length=2000, null=True)
    deleted=models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    @staticmethod
    def all_todos():
        return Todo.objects.filter(deleted=False);






class UserTask(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    @staticmethod
    def find_all():
        return UserTask.objects.all();

    @staticmethod
    def find_by_user(user):
        try:
            return UserTask.objects.filter(user=user,deleted=False)
        except Exception as e:
            print(traceback.format_exc())
            return None

    @staticmethod
    def find_by_task(task):
        try:
            return UserTask.objects.filter(task=task, deleted=False)
        except Exception as e:
            print(traceback.format_exc())
            return None



#    Object Types





