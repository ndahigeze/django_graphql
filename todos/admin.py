from django.contrib import admin

# Register your models here.
from todos.models import Task, Todo, UserTask

admin.site.register(Task)
admin.site.register(Todo)
admin.site.register(UserTask)
