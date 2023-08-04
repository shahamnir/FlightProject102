from ..models import Country, Airline
from ..serializers import CountrySerializer, AirlineSerializer
from rest_framework.generics import (
    ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
)
from rest_framework.views import APIView
from ..AirlineFunctions import ( 
    get_airline_by_username, get_airlines_by_country,
    get_airline_name_by_id, get_country_name_by_id
)
from ..AirlineFacade import AirlineFacade


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

"""
Airline Facade View
"""
class DetailsAirline(APIView):
    def put(self, request, pk):
        response = AirlineFacade.update_airline(request, pk)
        return response


"""
More airline related views:
"""

class GetAirlineByUsername(APIView):
    def get(self, request):
        response = get_airline_by_username(request)
        return response

  
class GetAirlinesByCountry(APIView):
    def get(self, request):
        response = get_airlines_by_country(request)
        return response


class GetAirlineNameByID(APIView):
    def post(self, request):
        response = get_airline_name_by_id(request)
        return response


class GetCountryNameByID(APIView):
    def post(self, request):
        response = get_country_name_by_id(request)
        return response
