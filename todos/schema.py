import graphene
from django.utils.decorators import method_decorator
from graphene_django import DjangoListField
from graphql_jwt.decorators import login_required

from todos.models import Task, Todo
from todos.mutations import SaveTaskMutation, SaveTodoMutation
from todos.object_types import TaskType, TodoType


class TodosQuery(graphene.ObjectType):
    tasks = graphene.List(TaskType)
    todos = graphene.List(TodoType)

    @login_required
    def resolve_tasks(self,info,**kwargs):
        return Task.all_tasks()

    @login_required
    def resolve_todos(self,info,**kwargs):
        return Todo.all_todos()



class TodosMutations(graphene.ObjectType):
    save_task = SaveTaskMutation.Field()
    save_todo = SaveTodoMutation.Field()


# schema = graphene.Schema(query=TodosQuery,mutation=TodosMutations)