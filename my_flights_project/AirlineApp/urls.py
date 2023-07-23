from django.urls import path
from . import views

app_name = "AirlineApp"
urlpatterns = [
    path('country/', views.CountryList.as_view(),),
    path('country/<int:pk>/', views.CountryDetails.as_view(),),
    path('list/', views.AirlineList.as_view(),),
    path('create/', views.AirlineCreate.as_view(),),
    path('flights/', views.FlightsList.as_view(),),
    path('flights/<int:pk>/', views.FlightDetails.as_view(),),
    path('flights_by_params/', views.GetFlightsByParams.as_view(),),
    path('airlines_by_username/', views.GetAirlineByUsername.as_view(),),
    path('flights_by_airline/', views.GetFlightsByAirline.as_view(),),
    path('departure_flights/', views.GetDepartureFlights.as_view(),),
    path('arrival_flights/', views.GetArrivalFlights.as_view(),),
    path('airlines_by_country/', views.GetAirlinesByCountry.as_view(),),
    path('flights_by_origin_country/', views.GetFlightsByOriginCountry.as_view()),
    path('flights_by_destination_country/', views.GetFlightsByDestinationCountry.as_view(),),
    path('flights_by_departure_date/', views.GetFlightsByDepartureDate.as_view(),),
    path('flights_by_landing_date/', views.GetFlightsByLandingDate.as_view(),),
    path('my_flights/', views.GetMyFlights.as_view(),),
    path('details_airline/<int:pk>/', views.DetailsAirline.as_view(),),
    path('add_flight/', views.AddFlight.as_view()),
    path('details_flight/<int:pk>/', views.DetailsFlight.as_view(),),
    path('airline_name_by_id/', views.GetAirlineNameByID.as_view()),
    path('country_name_by_id/', views.GetCountryNameByID.as_view()),
]
