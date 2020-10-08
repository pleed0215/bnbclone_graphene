import graphene
from graphene.types.argument import Argument

from .models import User


class CreateAccountMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        password = graphene.String(required = True)
        email = graphene.String(required = True)

    ok = graphene.Boolean()
    error = graphene.String()

    #def mutate(self, info, *args, **kwargs):
    def mutate(self, info, email, password, first_name, last_name):
        try:
            User.objects.get(email=email)
            return CreateAccountMutation(ok=False, error="User arleady exist.")
        except User.DoesNotExist:
            try:
                User.objects.create_user(email, email, password)
                return CreateAccountMutation(ok=True)
            except:
                return CreateAccountMutation(ok=False, error="Can't create user account.")
            