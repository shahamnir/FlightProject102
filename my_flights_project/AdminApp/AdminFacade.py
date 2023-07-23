from CustomerApp.models import Custumer
from CustomerApp.serializers import CustomerSerializer
from rest_framework.response import Response
from AirlineApp.serializers import AirlineSerializer
from AirlineApp.models import Airline
from .serializers import AdministratorSerializer
from .models import Administrator
from django.views.decorators.csrf import csrf_exempt


class AdminFacade():
    def get_all_customers(request):
        customers = Custumer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        response = Response(serializer.data, status=200)
        return response
      
    @csrf_exempt
    def add_airline(request):
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=201)
        else:
            response = Response(serializer.errors, status=400)
        return response
    
    def add_customer(request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=201)
        else:
            response = Response(serializer.errors, status=400)
        return response
    
    def add_administrator(request):
        serializer = AdministratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=201)
        else:
            response = Response(serializer.errors, status=400)
        return response

    def remove_airline(request, pk):
        airline = Airline.objects.get(pk=pk)
        airline.delete()
        response = Response(status=200)
        return response
    
    def remove_customer(request, pk):
        customer = Custumer.objects.get(pk=pk)
        customer.delete()
        response = Response(status=200)
        return response
  
    def remove_administrator(request, pk):
        administrator = Administrator.objects.get(pk=pk)
        administrator.delete()
        response = Response(status=200)
        return response
