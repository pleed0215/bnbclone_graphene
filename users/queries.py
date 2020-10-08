from .types import UserListResponse
from .models import User


def resolve_users(self, info, page=1):
    page = page > 0 and page or 1
    print(page)
    page_size = 20
    model_count = User.objects.count()
    start_index = (page-1)*page_size
    last_count = 0
    if model_count <= page*page_size:
        last_count = model_count
    else:
        last_count = page*page_size
    query_rooms =  User.objects.all()[start_index:last_count]
    return UserListResponse(list=query_rooms, total=model_count, page=page, page_size = page_size)

def resolve_user(self, info, id):
    if id is not None:
        try:
            user = User.objects.get(pk=id)
            return user
        except User.DoesNotExist:
            return None