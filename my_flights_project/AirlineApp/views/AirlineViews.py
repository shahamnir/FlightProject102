from ..models import Country, Airline, Flights
from ..serializers import CountrySerializer, AirlineSerializer, FlightSerializer
from rest_framework.generics import (
    ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView, CreateAPIView,GenericAPIView
)
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from ..AirlineFacade import (
    get_flights_by_params,get_airlines_by_params,get_airline_by_username, get_flights_by_airline,
    get_arrival_flights,get_departure_flights
    )






class CountryList(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class AirlineList(ListAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class AirlineCreate(CreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class AirlineDetails(RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class GetAirlineByParams(APIView):
    def get(self, request):
        name = request.data.get('name')
        country = request.data.get('country')
        
        airline = get_airlines_by_params(name=name,country=country)
        serializer = AirlineSerializer(airline,many=True)
        return Response(serializer.data, status=200)
    

class GetAirlineByUsername(APIView):
    def get(self,request):
        username = request.data.get('username')
        airline = get_airline_by_username(username=username)
        serializer = AirlineSerializer(airline,many=True)
        return Response(serializer.data, status=200)
    
class GetAirlinesByCountry(APIView):
    def get(self,request):
        country_id = request.data.get('country_id')
        airlines = Airline.objects.filter(country_id=country_id)
        serializer = AirlineSerializer(airlines,many=True)
        return Response(serializer.data,status=200)