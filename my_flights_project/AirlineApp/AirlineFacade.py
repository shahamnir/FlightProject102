from .models import Flights, Airline
from .serializers import FlightSerializer, AirlineSerializer
from rest_framework.response import Response


class AirlineFacade():

    """
    Update airline instance according to a pk
    """
    def update_airline(request, pk):
        airline = Airline.objects.get(pk=pk)
        serializer = AirlineSerializer(airline, request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=200)
        else:
            response = Response(serializer.errors, status=400)
        return response

    def add_flight(request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=201)
        else:
            response = Response(serializer.errors, status=400)
        return response
    
    def update_flight(request, pk):
        flight = Flights.objects.get(pk=pk)
        serializer = FlightSerializer(flight, request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=200)
        else:
            response = Response(serializer.errors, status=400)
        return response

    def get_my_flights(request):
        airline_id = request.data.get('airline_id')
        flights = Flights.objects.filter(airline_id=airline_id)
        serializer = FlightSerializer(flights, many=True)
        response = Response(serializer.data, status=200)
        return response

    def remove_flight(request, pk):
        flight = Flights.objects.get(pk=pk)
        flight.delete()
        response = Response(status=200)
        return response
