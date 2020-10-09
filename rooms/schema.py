import graphene
from graphene_django import DjangoObjectType

from .models import Room

from users.schema import UserType
from .types import RoomType, RoomListResponse


class Query(graphene.ObjectType):
    #rooms = graphene.List(RoomType, page=graphene.Int())
    rooms = graphene.Field(RoomListResponse, page=graphene.Int())
    room =graphene.Field(RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        print(info.context.user)
        page = page > 0 and page or 1
        print(page)
        page_size = 50
        model_count = Room.objects.count()
        start_index = (page-1)*page_size
        last_count = 0
        if model_count <= page*page_size:
            last_count = model_count
        else:
            last_count = page*page_size
        query_rooms =  Room.objects.all()[start_index:last_count]
        return RoomListResponse(list=query_rooms, total=model_count, page=page)

    def resolve_room(self, info, id):
        if id is not None:
            try:
                room = Room.objects.get(pk=id)
                return room
            except Room.DoesNotExist:
                return None