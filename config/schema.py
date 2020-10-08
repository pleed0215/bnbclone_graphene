import graphene
from graphene_django import DjangoObjectType
from rooms import schema as rooms_schema
from users import schema as users_schema


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



class Query(rooms_schema.Query, users_schema.Query, graphene.ObjectType):
    pass


class Mutation(users_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)