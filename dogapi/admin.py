from django.contrib import admin
from .models import Dog

# Register your models here.
class DogAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'age', 'owner')
    
    # Add search functionality for specific fields
    search_fields = ('name', 'owner')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('age', 'owner')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name',)

    # Define how fields are displayed when editing a Dog instance
    fields = ('owner', 'name', 'age')

# Register the model and admin class
admin.site.register(Dog, DogAdmin)