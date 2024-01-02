from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def contact_us(request):
    return render(request, 'contact_us.html')