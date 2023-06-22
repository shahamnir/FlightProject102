from typing import Any
from django.db import models
from AdminApp.models import User
from AirlineApp.models import Flights



class Custumer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    credit_card_no = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=3)


class Ticket(models.Model):
    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    customer = models.ForeignKey(Custumer,on_delete=models.CASCADE)





