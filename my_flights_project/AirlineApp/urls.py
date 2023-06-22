from django.urls import path
from . import views

app_name = "AirlineApp"
urlpatterns = [
    path('country/',views.CountryList.as_view(),name="country_list"),
    path('country/<int:pk>/',views.CountryDetails.as_view(),name="country_details"),
    path('list/',views.AirlineList.as_view(),name="airline_list"),
    path('create/',views.AirlineCreate.as_view(),name="airline_create"),
    path('airline/<int:pk>/',views.AirlineDetails.as_view(),name="airline_details"),
    path('flights/',views.FlightsList.as_view(),name="flights_list"),
    path('flights/<int:pk>/',views.FlightDetails.as_view(),name="flights_details"),
    path('flights_by_params/',views.GetFlightsByParams.as_view(),name="flights_by_params"),
    path('airlines_by_params/',views.GetAirlineByParams.as_view(),name="airlines_by_params"),
    path('airlines_by_username/',views.GetAirlineByUsername.as_view(),name="airlines_by_username"),
    path('flights_by_airline/',views.GetFlightsByAirline.as_view(),name="flights_by_airline"),
    path('departure_flights/',views.GetDepartureFlights.as_view(),name="departure_flights"),
    path('arrival_flights/',views.GetArrivalFlights.as_view(),name="arrival_flights"),
    path('airlines_by_country/',views.GetAirlinesByCountry.as_view(),name="airlines_by_country"),
    path('flights_by_origin_country/',views.GetFlightsByOriginCountry.as_view(),name="flights_by_origin_country"),
    path('flights_by_destination_country/',views.GetFlightsByDestinationCountry.as_view(),name="flights_by_destination_country"),
    path('flights_by_departure_date/',views.GetFlightsByDepartureDate.as_view(),name="flights_by_departure_date"),
    path('flights_by_landing_date/',views.GetFlightsByLandingDate.as_view(),name="flights_by_landing_date"),
    
]