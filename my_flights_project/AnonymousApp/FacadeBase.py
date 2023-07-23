from datetime import datetime
from AirlineApp.models import Flights, Airline, Country
from AirlineApp.serializers import ( 
    FlightSerializer, AirlineSerializer, CountrySerializer)
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from CustomerApp.models import Custumer
from CustomerApp.serializers import CustomerSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class FacadeBase():

    def get_all_flights(request):
        flights = Flights.objects.all()
        serializer = FlightSerializer(flights, many=True)
        response = Response(serializer.data, status=200)
        return response
    
    def get_flight_by_id(request, pk):
        try:
            flight = Flights.objects.get(pk=pk)
            serializer = FlightSerializer(flight)
            response = Response(serializer.data, status=200)
            return response
        except Flights.DoesNotExist:
            response_data = {'error': 'Flight does not exist'}
            response = Response(response_data, status=404)
            return response

    def get_flights_by_params(request):
        
        origin_country = request.GET.get('origin_country')
        origin_country_instance = Country.objects.filter(
                                    name=origin_country).first()
        origin_country_id = origin_country_instance.id
        destination_country = request.GET.get('destination_country')
        destination_country_intance = Country.objects.filter(
                                    name=destination_country).first()
        destination_country_id = destination_country_intance.id
        date_str = request.GET.get('departure_date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        flights = Flights.objects.filter(
            origin_country_id=origin_country_id,
            destination_country_id=destination_country_id,
            departure_time__date=date)
        serializer = FlightSerializer(flights, many=True)
        response = Response(serializer.data, status=200)
        return response

    def get_all_airlines(request):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        response = Response(serializer.data, status=200)
        return response
    
    def get_airline_by_id(request, pk):
        airline = Airline.objects.get(pk=pk)
        serializer = AirlineSerializer(airline)
        response = Response(serializer.data, status=200)
        return response
    
    def get_airline_by_params(request):
        country_name = request.GET.get('country')
        try:
            country = Country.objects.filter(name=country_name).first()
            airlines = Airline.objects.filter(country_id=country.id)
            serializer = AirlineSerializer(airlines, many=True)
            return Response(serializer.data, status=200)
        except ObjectDoesNotExist:
            response_data = {'error': 'Country does not exist'}
            return Response(response_data, status=404)
    
    def get_all_countries(request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        response = Response(serializer.data, status=200)
        return response
    
    def get_country_by_id(request, pk):
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country)
        response = Response(serializer.data, status=200)
        return response
    
    def add_customer(request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=201)
        else:
            response = Response(serializer.errors, status=400)
        return response
    
    def register(request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            response = Response({
                'message': 'Username, password, and email are required.'
                },
                status=400)

        try:
            customer = Custumer(username=username, password=password,
                                email=email, user_role=3)
            customer.save()
            response = Response({'message': 'Registration successful'})
        except Exception as e:
            response = Response({
                'message': 'Registration failed: {}'.format(str(e))
                },
                status=400)

        return response
