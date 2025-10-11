import graphene
from graphene_django.types import DjangoObjectType
from dogapi.models import Dog
from graphql import GraphQLError
from django.contrib.auth import get_user_model
import graphql_jwt

class DogType(DjangoObjectType):
    class Meta:
        model = Dog

# class Query(graphene.ObjectType):
#     dog = graphene.Field(DogType, id=graphene.Int())

#     def resolve_dog(self, info, id):
#         user = info.context.user
#         if user.is_anonymous:
#             raise GraphQLError('Not authenticated')
#         try:
#             dog = Dog.objects.get(pk=id)
#             if dog.owner != user:
#                 raise GraphQLError('You do not have permission to view this dog.')
#             return dog
#         except Dog.DoesNotExist:
#             return None
        
# class Mutation(graphene.ObjectType):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()

# schema = graphene.Schema(query=Query, mutation=Mutation)