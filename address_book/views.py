from django.shortcuts import render

# Create your views here.

# HOME PAGE
def home(request):
	return render(request, 'home.html', {})

# ADD ADDRESS PAGE
def add_address(request):
	return render(request, 'add_address.html', {})
