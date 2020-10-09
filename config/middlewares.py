import jwt
from django.conf import settings

from users.models import User

class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        request = info.context
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header is not None:
            try:
                x_token, token = auth_header.split(" ")
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
                pk = decoded.get('pk')
                user = User.objects.get(pk=pk)
                info.context.user = user
            except User.DoesNotExist:
                pass

        return next(root, info, **args)