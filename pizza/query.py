import graphene
from graphene_django import DjangoObjectType
from django.db import models

from django.db.models import Q

from .models import Pizza
from .types import PizzaType

class Query(graphene.ObjectType):
    pizza = graphene.List(
        PizzaType,
        name = graphene.String(),
        id = graphene.ID(),
        first=graphene.Int(),
        skip=graphene.Int(),
        )

    def resolve_pizza(self, info, first=None, skip=None, name=None, id=None, **kwargs):
        show = Pizza.objects.all()
        
        if name:
            show = show.filter(Q(name__icontains = name))
        if id:
            show = show.filter(Q(name__icontains = id))
        
        if skip:
            show = show[skip::]
        
        if first:
            show = show[:first]
        
        return show
        