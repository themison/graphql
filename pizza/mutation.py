import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from graphql_jwt.decorators import login_required

from .models import Pizza
from .types import PizzaType

class CreatePizza(graphene.Mutation):
    pizza = graphene.Field(PizzaType)

    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Int(required=True)
        description = graphene.String(required=True)
    
    @login_required
    def mutate(self, info, name, price, description):
        pizza = Pizza(
            name=name,
            price=price,
            description=description
        )
        pizza.save()

        return CreatePizza(pizza=pizza)


class UpdatePizza(graphene.Mutation):
    pizza = graphene.Field(PizzaType)

    class Arguments:    
        id = graphene.ID(required=True)
        name = graphene.String()
        price = graphene.Int()
        description = graphene.String()
    @login_required
    def mutate(self, info, id, name=None, price=None, description=None):
        pizza = Pizza.objects.get(id=id)

        if name:
            pizza.name = name
        if price:
            pizza.price = price
        if description:
            pizza.description = description
        pizza.save()
        print(123)

        return UpdatePizza(pizza=pizza)



class DeletePizza(graphene.Mutation):
    pizza = graphene.Field(PizzaType)

    class Arguments:
        id = graphene.Int()
    
    @login_required
    def mutate(self, info, id):
        pizza = Pizza.objects.get(id=id)
        pizza.delete()

    # return ("Pizza was deleted")


class Mutation(graphene.ObjectType):
    create_pizza = CreatePizza.Field()
    update_pizza = UpdatePizza.Field()
    delete_pizza = DeletePizza.Field()
