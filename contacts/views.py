from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)

        contact.save()

        # SEND EMAIL
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign in to the admin panel for more information.',
            'realestate@gmail.com',
            [realtor_email, ],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
