from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from graphql_jwt.shortcuts import get_token
from graphene_django import DjangoObjectType
from django_redis import get_redis_connection
import graphene


from .types import UserType

class Register(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class ResetPassword(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = get_user_model()(
            username=username,
        )
        user.set_password(password)

        return ResetPassword(user=user)


class Login(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()

    class Arguments():
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = authenticate(username = username,password = password)
        token = get_token(user)

        return Login(user=user, token=token)

class Logout(graphene.Mutation):
    token = graphene.String()

    class Arguments():
        token = graphene.String(required=True)

    def mutate(self,info,token):
        con = get_redis_connection("default")
        con.sadd("tokens",token)
        

        return Logout(token=token)


class Mutation(graphene.ObjectType):
    login = Login.Field()
    register = Register.Field()
    reset_password = ResetPassword.Field()
    logout = Logout.Field()