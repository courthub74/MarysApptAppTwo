from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ["firstname", "lastname", "email", "phone", "occupation", "category", "day", "month", "date", "year", "time", "ampm", "location", "address", "city", "state", "zipcode",]

# Split these classess maybe call it LocationForm and then add the addy etc.