from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SizeChoices(models.TextChoices):
    Tiny = "TY", "Tiny"
    Small = "SL", "Small"
    Medium = "MD", "Medium"
    Large = "LG", "Large"

class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(
        max_length=10,
        choices=SizeChoices.choices,
        default=SizeChoices.Medium
    )
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()
    

    def __str__(self):
        return self.name
    
class Dog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favfood = models.CharField(max_length=100)
    favtoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
