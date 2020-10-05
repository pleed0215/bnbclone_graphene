import graphene
from graphene_django import DjangoObjectType

from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser')

class UserListResponse(graphene.ObjectType):
    list = graphene.List(UserType)
    total = graphene.Int()
    page = graphene.Int()
    page_size = graphene.Int()