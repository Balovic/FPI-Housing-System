from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.utils import timezone


class Listing(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    )

    GARAGE_TYPE_CHOICES = (
        ('Garage_available', 'Yes'),
        ('Garage_unavailable', 'No'),
    )

    PARKING_TYPE_CHOICES = (
        ('Parking_available', 'Yes'),
        ('Parking_unavailable', 'No'),
    )


    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    small_des = models.CharField(max_length=200)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.CharField(max_length=200, choices=GARAGE_TYPE_CHOICES)
    parking = models.CharField(max_length=200, choices=PARKING_TYPE_CHOICES)
    sqft = models.IntegerField(default=0)
    property_type = models.CharField(max_length=4, choices = PROPERTY_TYPE_CHOICES)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now)
    is_sold = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class City(models.Model):
    city_name = models.CharField(max_length=200, unique=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    properties_no = models.IntegerField(default=0)

    def __str__(self):
        return self.city_name

class HouseInquiry(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    message = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inquiry for {self.listing.title}"

