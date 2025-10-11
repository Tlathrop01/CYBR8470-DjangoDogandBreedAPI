from django.contrib import admin
from .models import Breed, Dog

# Register your models here.
class DogAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'age', 'owner')
    
    # Add search functionality for specific fields
    search_fields = ('name', 'owner')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('age', 'breed')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name', 'owner')

    # Define how fields are displayed when editing a Dog instance
    fields = ('owner', 'name', 'age', 'breed')

# Register the model and admin class
admin.site.register(Dog, DogAdmin)

class BreedAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'size')
    
    # Add search functionality for specific fields
    search_fields = ('name', 'size', 'friendliness')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('name', 'friendliness')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name', 'size')

    # Define how fields are displayed when editing a Dog instance
    fields = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')

# Register the model and admin class
admin.site.register(Breed, BreedAdmin)