from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required

import graphene
from graphene_django import DjangoObjectType
from .types import UserType

class Query(graphene.AbstractType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    @login_required
    def resolve_users(self, info):
        return User.objects.all()


    @login_required 
    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged!')

        return user