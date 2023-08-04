from .models import Flights, Country, Airline
from django.utils import timezone
from datetime import timedelta, datetime
from .serializers import FlightSerializer, AirlineSerializer, CountrySerializer
from rest_framework.response import Response

"""
Get a
"""
def get_airline_by_username(request):
    username = request.data.get('username')
    airline = Airline.objects.filter(username=username)
    serializer = AirlineSerializer(airline, many=True)
    response = Response(serializer.data, status=200)
    return response


def get_airlines_by_country(request):
    country_id = request.data.get('country_id')
    airlines = Airline.objects.filter(country_id=country_id)
    serializer = AirlineSerializer(airlines, many=True)
    response = Response(serializer.data, status=200)
    return response


def get_flights_by_params(request):
    origin_country_id = request.data.get('origin_country_id')
    destination_country_id = request.data.get('destination_country_id')
    departure_time = request.data.get('departure_time')
    flights = Flights.objects.filter(
                                origin_country_id=origin_country_id,
                                destination_country_id=destination_country_id,
                                departure_time=departure_time)         
    serializer = FlightSerializer(flights, many=True)
    response = Response(serializer.data, status=200)
    return response


def get_flights_by_airline(request):
    airline_id = request.data.get('airline_id')
    flights = Flights.objects.filter(airline_id=airline_id)
    serializer = FlightSerializer(flights, many=True)
    response = Response(serializer.data, status=200)
    return response


"""
Function to get flights arriving within the next 12 hours in a specific destination country
"""
def get_arrival_flights(request):
    destination_country = request.data.get('destination_country')
    current_time = timezone.now()
    time_limit = current_time + timedelta(hours=12)
    flights = Flights.objects.filter(landing_time__gte=current_time,
                                     landing_time__lte=time_limit,
                                     destination_country=destination_country)
    serializer = FlightSerializer(flights, many=True)
    response = Response(serializer.data, status=200)
    return response

"""
Function to get flights departing within the next 12 hours from a specific origin country
"""
def get_departure_flights(request):
    origin_country = request.data.get('origin_country')
    current_time = timezone.now()
    time_limit = current_time + timedelta(hours=12)
    flights = Flights.objects.filter(departure_time__gte=current_time,
                                     departure_time__lte=time_limit,
                                     origin_country=origin_country)
    serializer = FlightSerializer(flights, many=True)
    response = Response(serializer.data, status=200)
    return response


def get_flight_by_origin_country(request):
    origin_country = request.data.get('origin_country')
    flights = Flights.objects.filter(origin_country=origin_country)
    serializer = FlightSerializer(flights, many=True)
    respone = Response(serializer.data, status=200)
    return respone


def get_flights_by_destination_country(request):
    destination_country = request.data.get('destination_country')
    flights = Flights.objects.filter(destination_country=destination_country)
    serializer = FlightSerializer(flights, many=True)
    response = Response(serializer.data, status=200)      
    return response


def get_flights_by_departure_date(request):
    date_str = request.data.get('departure_date')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    flights = Flights.objects.filter(departure_time__date=date)
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data, status=200)


def get_flights_by_landing_date(request):
    date_str = request.data.get('landing_date')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    flights = Flights.objects.filter(landing_time__date=date)
    serializer = FlightSerializer(flights, many=True)
    response = Response(serializer.data, status=200)
    return response


def get_airline_name_by_id(request):
    pk = request.data.get('id')
    airline = Airline.objects.get(pk=pk)
    serializer = AirlineSerializer(airline)
    name = serializer.data.get('name')
    response_data = {'name': name}
    response = Response(response_data, status=200)
    return response


def get_country_name_by_id(request):
    pk = request.data.get('id')
    country = Country.objects.get(pk=pk)
    serializer = CountrySerializer(country)
    name = serializer.data.get('name')
    response_data = {'name': name}
    response = Response(response_data, status=200)
    return response

