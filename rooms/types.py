import graphene
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import Room

class RoomType(DjangoObjectType):
    user = graphene.Field(type=UserType)
    is_fav = graphene.Boolean()
    class Meta:
        model = Room

    def resolve_is_fav(parent, info):
        user = info.context.user
        if user is not None and user.is_authenticated:
            return parent in user.favs.all()
        return None

class RoomListResponse(graphene.ObjectType):
    list = graphene.List(RoomType)
    total = graphene.Int()
    page = graphene.Int()


class RoomListType(graphene.ObjectType):
    list = graphene.List(RoomType)