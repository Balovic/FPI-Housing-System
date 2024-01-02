from django.contrib import admin

from .models import Listing, City

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'property_type', 'is_published', 'price', 'date_added', 'realtor', 'is_sold', 'is_rented')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'property_type', 'is_sold', 'is_rented')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
admin.site.register(City)

