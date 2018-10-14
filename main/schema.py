import graphene

import pizza.query
import pizza.mutation


class Query(pizza.query.Query, graphene.ObjectType):
    pass

class Mutation(pizza.mutation.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)