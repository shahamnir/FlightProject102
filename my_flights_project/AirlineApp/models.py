from django.db import models
from AdminApp.models import User,UserRole
from django.utils import timezone



class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)



class Airline(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=2)

class Flights(models.Model):

    airline = models.ForeignKey(Airline,on_delete=models.CASCADE)
    origin_country = models.ForeignKey(Country,related_name='origin_country',on_delete=models.CASCADE)
    destination_country = models.ForeignKey(Country,related_name='destination_country',on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    remaining_tickets = models.PositiveIntegerField()

        
