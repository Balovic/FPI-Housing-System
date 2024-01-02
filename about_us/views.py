from django.shortcuts import render, get_object_or_404

# Create your views here.

def about_us(request):
    return render(request, 'about_Us.html')