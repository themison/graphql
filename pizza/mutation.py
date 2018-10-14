import graphene
from graphene_django import DjangoObjectType
from django.db import models

from .models import Pizza

class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza


class CreatePizza(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Int()

    class Arguments:
        name = graphene.String()
        price = graphene.Int()
    
    def mutate(self, info, name, price):
        pizza = Pizza(name = name, price = price)
        pizza.save()

        return CreatePizza(
            id = pizza.id,
            name = pizza.name,
            price = pizza.price,
        )

class UpdatePizza(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Int()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
    
    def mutate(self, info, id, name, price):
        pizza = Pizza(name = name, price = price)
        pizza.save()
        return UpdatePizza(
            id = pizza.id,
            name = pizza.name,
            price = pizza.price)
      

class DeletePizza(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Int()

    class Arguments:
        id = graphene.Int()
    
    def mutate(self, info, id):
        pizza = Pizza(id = id)
        pizza.delete()
        return DeletePizza(
            id = pizza.id,
            name = pizza.name,
            price = pizza.price,
        )



class Mutation(graphene.ObjectType):
    create_pizza = CreatePizza.Field()
    update_pizza = UpdatePizza.Field()
    delete_pizza = DeletePizza.Field()
