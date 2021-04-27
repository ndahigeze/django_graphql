import graphene
from graphql_auth import mutations
# from graphql_auth.decorators import login_required
from graphql_jwt.decorators import login_required

from accounts.schema import AuthMutation
from todos.models import Task, Todo
from todos.object_types import TaskType, TodoType


class SaveTaskMutation(graphene.Mutation):

    task = graphene.Field(TaskType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        start_date = graphene.String(required=True,)
        end_date = graphene.String(required=True)

    @classmethod
    @login_required
    def mutate(cls,root,info,name,description,start_date,end_date):
        task = Task(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        task.save()
        return SaveTaskMutation(task=task)




class SaveTodoMutation(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        start_date = graphene.String(required=True, )
        end_date = graphene.String(required=True)
        task_id= graphene.Int(required=True)

    @classmethod
    @login_required
    def mutate(cls,root,info,name,description,start_date,end_date,task_id ):
        task=Task.objects.get(pk=task_id)
        todo = Todo(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            task=task
        )
        todo.save()
        return SaveTodoMutation(todo=todo)





