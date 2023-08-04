from ..models import Flights
from ..serializers import FlightSerializer
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)
from rest_framework.views import APIView
from ..AirlineFunctions import (
    get_flights_by_params, get_flights_by_airline,
    get_arrival_flights, get_departure_flights,
    get_flight_by_origin_country, get_flights_by_destination_country, 
    get_flights_by_departure_date, get_flights_by_landing_date
    )
from ..AirlineFacade import AirlineFacade


class FlightsList(ListCreateAPIView):
    queryset = Flights.objects.all()
    serializer_class = FlightSerializer


class FlightDetails(RetrieveUpdateDestroyAPIView):
    queryset = Flights.objects.all()
    serializer_class = FlightSerializer


"""
Airline Facade Views:
"""

class AddFlight(APIView):
    def post(self, request):
        response = AirlineFacade.add_flight(request)
        return response
    

class DetailsFlight(APIView):  
    def put(self, request, pk):
        response = AirlineFacade.update_flight(request, pk)
        return response
    
    def delete(self, request, pk):
        response = AirlineFacade.remove_flight(request, pk)
        return response


class GetMyFlights(APIView):
    def get(self, request):
        response = AirlineFacade.get_my_flights(request)
        return response


"""
More flights related views:
"""

class GetFlightsByParams(APIView):
    def get(self, request):
        response = get_flights_by_params(request)
        return response


class GetFlightsByAirline(APIView):
    def get(self, request):
        response = get_flights_by_airline(request)
        return response


class GetArrivalFlights(APIView):
    def get(self, request):
        response = get_arrival_flights(request)
        return response


class GetDepartureFlights(APIView):
    def get(self, request):
        response = get_departure_flights(request)
        return response


class GetFlightsByOriginCountry(APIView):
    def get(self, request):
        response = get_flight_by_origin_country(request)
        return response


class GetFlightsByDestinationCountry(APIView):
    def get(self, request):
        response = get_flights_by_destination_country(request)
        return response


class GetFlightsByDepartureDate(APIView):
    def get(self, request):
        response = get_flights_by_departure_date(request)
        return response


class GetFlightsByLandingDate(APIView):
    def get(self, request):
        response = get_flights_by_landing_date(request)
        return response






    

    








    
  





    


