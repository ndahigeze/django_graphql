from graphene_django import DjangoObjectType

from todos.models import Todo, Task, UserTask


class TodoType(DjangoObjectType):
    class Meta:
        model= Todo
        fields =  "__all__"


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = "__all__"


class UserTaskType(DjangoObjectType):

    class Meta:
        model = UserTask
        fields = "__all__"



