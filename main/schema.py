import graphene
import graphql_jwt

import users.mutation
import users.query
import pizza.query
import pizza.mutation


class Query(pizza.query.Query, users.query.Query, graphene.ObjectType):
    pass

class Mutation(pizza.mutation.Mutation, users.mutation.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)