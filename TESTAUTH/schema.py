

import graphene

import accounts
import todos
from todos.schema import TodosQuery, TodosMutations


class Query(
    accounts.schema.Query,
    TodosQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    accounts.schema.Mutation,
    TodosMutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)