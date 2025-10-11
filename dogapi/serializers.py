from rest_framework import serializers
from .models import Dog, Breed

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'owner']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']