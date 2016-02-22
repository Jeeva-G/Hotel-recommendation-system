"""Importing the model classes here."""
from django.contrib import admin
from .models import Hotel, Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    """Importing the two classes we defined and registering them."""

    model = Review
    list_display = ('Hotel', 'rating', 'user_name', 'comment', 'pub_date')
    # Adding a sort option on the below fields.
    list_filter = ['pub_date', 'user_name']
    # Creating a search on the comment field.
    search_fields = ['comment']

admin.site.register(Hotel)
admin.site.register(Review, ReviewAdmin)
