import graphene
from graphene_django import DjangoObjectType
from rooms.models import Room
from users.models import User


# class RoomType(graphene.ObjectType):
"""name = graphene.String()
    address = graphene.String()
    price = graphene.Int()
    beds = graphene.Int()
    lat = graphene.Float()
    lng = graphene.Float()
    bedrooms = graphene.Int()
    bathrooms = graphene.Int()
    check_in = graphene.DateTime()
    check_out = graphene.DateTime()
    instant_book = graphene.Boolean()"""


class UserType(DjangoObjectType):
    class Meta:
        model = User


class RoomType(DjangoObjectType):
    user = graphene.Field(type=UserType)

    class Meta:
        model = Room


class Query(graphene.ObjectType):
    hello = graphene.String()
    rooms = graphene.List(RoomType)

    def resolve_hello(self, info):
        return "Hello"

    def resolve_rooms(self, info):
        return Room.objects.all()


class Mutation:
    pass


schema = graphene.Schema(query=Query)