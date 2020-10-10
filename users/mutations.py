from django.contrib.auth import authenticate
from django.conf import settings

import jwt
import graphene
from graphene.types.argument import Argument

from .models import User
from .types import UserType


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
            
class LoginMutation(graphene.Mutation):
    class Arguments:
        email =  graphene.String()
        password = graphene.String()
    
    token = graphene.String()
    error = graphene.String()
    pk = graphene.Int()

    def mutate(self, info, email, password):
        user = authenticate(username=email, password=password)
        if user is not None:
            token = jwt.encode({'pk': user.pk}, settings.SECRET_KEY, algorithm='HS256')
            return LoginMutation(token=token.decode('utf-8'), pk=user.pk)
        else:
            return LoginMutation(token=None, error="Can't log in.")

class UpdateProfileMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    message = graphene.String()
    user = graphene.Field(UserType)

    def mutate(self, info, first_name=None, last_name=None, email=None):
        user = info.context.user
        print (user)
        if user is None or not user.is_authenticated:
            raise Exception("You need to be logged in")
        
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if email is not None and email != user.email:
            try:
                User.objects.get(email=email)
                return UpdateProfileMutation(ok=False, message="Email address you wrote is already exist. Use other email please.")
            except User.DoesNotExist:
                user.email = email
        user.save()
        return UpdateProfileMutation(ok=True, message="User information succefully updated", user=user)
