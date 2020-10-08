import graphene
from graphene_django import DjangoObjectType

from .models import User
from . import queries as resolvers
from .types import UserType, UserListResponse
from .mutations import CreateAccountMutation


class Query(graphene.ObjectType):
    users = graphene.Field(UserListResponse, page=graphene.Int(), resolver=resolvers.resolve_users)
    user = graphene.Field(UserType, id=graphene.Int(required=True), resolver=resolvers.resolve_user)

    

class Mutation(graphene.ObjectType):
    create_user = CreateAccountMutation.Field()

