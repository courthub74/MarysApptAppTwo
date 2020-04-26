from django.db import models

class Address(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=15)
	occupation = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	day = models.CharField(max_length=20)
	month = models.CharField(max_length=40)
	date = models.CharField(max_length=200)
	year = models.CharField(max_length=10)
	time = models.CharField(max_length=10)
	ampm = models.CharField(max_length=2)
	location = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=10)


	def __str__(self):
		return self.firstname
