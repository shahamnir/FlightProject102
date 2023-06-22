from .models import Flights,Country,Airline
from django.utils import timezone
from datetime import timedelta, datetime



def get_all_flights():
    flights = Flights.objects.all()
    return flights

def get_flight_by_id(id):
    flight = Flights.objects.get(id)
    return flight

def get_flights_by_params(origin_country_id,destination_country_id,departure_time):
    flight = Flights.objects.filter(origin_country_id=origin_country_id,
                                    destination_country_id=destination_country_id,
                                    departure_time=departure_time)
    return flight

def get_all_airlines():
    airlines = Airline.objects.all()
    return airlines

def get_airline_by_id(id):
    airline = Airline.objects.get(id)
    return airline

def get_airlines_by_params(name, country):
    airline = Airline.objects.filter(name=name,country=country)
    return airline

def get_all_countries():
    countries = Country.objects.all()
    return countries

def get_country_by_id(id):
    country = Country.objects.get(id)
    return country

def update_airline(airline):
    pass

def add_flight(flight):
    pass

def update_flight(flight):
    pass

def remove_flight(flight):
    pass

def get_my_flights():
    pass


def get_airline_by_username(username):
    airline = Airline.objects.filter(username=username)
    return airline


def get_flights_by_airline(airline_id):
    flights = Flights.objects.filter(airline_id=airline_id)
    return flights



def get_arrival_flights(destination_country):
    current_time = timezone.now()
    time_limit = current_time + timedelta(hours=12)
    flights = Flights.objects.filter(landing_time__gte=current_time,
                                     landing_time__lte=time_limit,
                                     destination_country=destination_country)
    return flights

def get_departure_flights(origin_country):
    current_time = timezone.now()
    time_limit = current_time + timedelta(hours=12)
    flights = Flights.objects.filter(departure_time__gte=current_time,
                                     departure_time__lte=time_limit,
                                     origin_country=origin_country)
    return flights



def get_departure_date(flight):
    departure_time_str = flight.departure_time
    departure_time = datetime.strptime(departure_time_str, '%Y-%m-%dT%H:%M:%SZ')
    departure_date = departure_time.date()

    return departure_date




