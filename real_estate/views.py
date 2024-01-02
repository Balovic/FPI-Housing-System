from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from listings.models import City

def home(request):
    house_list = Listing.objects.filter(property_type__in=['sale', 'rent'])

    context = {
        'house_list': house_list,
    }
    return render(request, 'home.html', context) 

# def listings_details(request, listing_id):
#     listing = get_object_or_404(Listing, pk=listing_id)
#     related_property = Listing.objects.filter(property_type__in=['sale'])

#     context = {
#         'listing': listing,
#         'related_property': related_property,
#     }

#     return render(request, 'listings/listing_details.html', context)