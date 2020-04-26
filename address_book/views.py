from django.shortcuts import render
from .models import Address 

# Create your views here.

# HOME PAGE
def home(request):
	all_addresses = Address.objects.all
	return render(request, 'home.html', {'all_addresses': all_addresses})

# ADD ADDRESS PAGE
def add_address(request):
	return render(request, 'add_address.html', {})
