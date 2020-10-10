import graphene
from .models import Room
from .types import RoomListType


class ToggleFavsMutation(graphene.Mutation):
    class Arguments:
        room_pk = graphene.Int(required=True)

    ok = graphene.Boolean()
    message = graphene.String()
    favs = graphene.Field(RoomListType)
        
    def mutate(self, info, room_pk):
        user = info.context.user

        if user is None or not user.is_authenticated:
            raise Exception("You need to logged in.")
        else:
            try:
                msg = ""
                room = Room.objects.get(pk=room_pk)
                if room in user.favs.all():
                    user.favs.remove(room)
                    msg = f"'{room}' is removed from your favorite list."
                else:
                    user.favs.add(room)
                    msg = f"'{room}' is added on your favorite list."
                return ToggleFavsMutation(ok=True, message=msg, favs=RoomListType(list=user.favs.all()))
            except Room.DoesNotExist:
                raise Exception(f"Not available with room pk: {room_pk}")
        