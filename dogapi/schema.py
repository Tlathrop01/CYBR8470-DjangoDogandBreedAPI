from graphene_django.types import DjangoObjectType
from dogapi.models import Dog



class DogType(DjangoObjectType):
    class Meta:
        model = Dog
