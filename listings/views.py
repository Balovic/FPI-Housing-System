from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import Listing, City

# Create your views here.

def listings(request):
    listings = Listing.objects.order_by('-date_added').filter(property_type__in=['sale', 'rent'])
    listing_count = listings.count() 
    city_list = City.objects.all()
    related_property = Listing.objects.filter(property_type__in=['sale'])

    paginator = Paginator(listings, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'listing_count': listing_count,
        'paginator': paginator,
        'city_list' : city_list,
        'related_property': related_property,
    }

    return render(request, 'listings/listings.html', context)

def listings_details(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    city_list = City.objects.all()
    related_property = Listing.objects.filter(property_type__in=['sale'])
    city_list = City.objects.all()

    context = {
        'listing': listing,
        'city_list': city_list,
        'related_property': related_property,
    }

    return render(request, 'listings/listing_details.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            listings = Listing.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(title__icontains=keyword))
            listings_count = Listing.count()
    context = {
        'listings': listings,
        'listings_count': listings_count,
    }
    return render(request, 'listings/listings.html', context)


# def search(request):
#     queryset_list = Listing.objects.order_by('-list_date')

#     # KEYWORDS
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_list = queryset_list.filter(description__icontains=keywords)

#     # CITY
#     if 'city' in request.GET:
#         city = request.GET['city']
#         if city:
#             queryset_list = queryset_list.filter(city__iexact=city)

#     # STATE
#     if 'state' in request.GET:
#         state = request.GET['state']
#         if state:
#             queryset_list = queryset_list.filter(state__iexact=state)

#     # BEDROOMS
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

#     # PRICE
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_list = queryset_list.filter(price__lte=price)

#     context = {
#         'state_choices': state_choices,
#         'bedroom_choices': bedroom_choices,
#         'price_choices': price_choices,
#         'listings': queryset_list,
#         'values': request.GET
#     }

#     return render(request, 'listings/listings.html', context)