import graphene
from graphene_django import DjangoObjectType
from django.db import models
from django.db.models import Q

from .models import Pizza

class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza

class Query(graphene.ObjectType):
    pizza = graphene.List(
        PizzaType,
        name = graphene.String(),
        id = graphene.ID(),)

    def resolve_pizza(self, info, name=None, id=None, **kwargs):
        if name:
            return Pizza.objects.filter(Q(name__icontains = name))
        if id:
            return Pizza.objects.filter(Q(id__icontains = id))
        return Pizza.objects.all()