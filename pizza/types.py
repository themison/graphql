from graphene_django import DjangoObjectType

from .models import Pizza

class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza
        exclude_fields = ('secret_key')
