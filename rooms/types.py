import graphene
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import Room

class RoomType(DjangoObjectType):
    user = graphene.Field(type=UserType)
    class Meta:
        model = Room

class RoomListResponse(graphene.ObjectType):
    list = graphene.List(RoomType)
    total = graphene.Int()
    page = graphene.Int()


class RoomListType(graphene.ObjectType):
    list = graphene.List(RoomType)