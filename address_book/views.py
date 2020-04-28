from django.shortcuts import render, redirect
from .models import Address 
from .forms import AddressForm
from django.contrib import messages

# Create your views here.
# The Functions for your actuall pages

# HOME PAGE
def home(request):
	all_addresses = Address.objects.all
	return render(request, 'home.html', {'all_addresses': all_addresses})

# ADD ADDRESS PAGE
def add_address(request):
	if request.method == 'POST': #<--IF THE REQUEST IS A POST OR SOMEONECLICKED THE BUTTON THEN:
		form = AddressForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Address Has Been Added!'))
			return redirect('home')
		else:
			messages.success(request, ('Seems Like There Was An Error...'))
			return render(request, 'add_address.html', {})
	else:
		return render(request, 'add_address.html', {})

#Split form and call it add_location where you just add the addy.  function reads (add_location)

# EDIT PAGE

