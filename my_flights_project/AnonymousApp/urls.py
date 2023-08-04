from django.urls import path, include
from . import views


app_name = "anonymous_app"
urlpatterns = [
    path('home', views.home, name="home"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('flights/', views.GetAllFlights.as_view(),),
    path('flights/<int:pk>/', views.GetFlightByID.as_view(),),
    path('flights_by_params/', views.GetFlightsByParams.as_view(),),
    path('airlines/', views.GetAllAirlines.as_view(),),
    path('airlines/<int:pk>/', views.GetAirlineByID.as_view(),),
    path('airline_by_params/', views.GetAirlineByParams.as_view(),),
    path('countries/', views.GetAllCountries.as_view(),),
    path('countries/<int:pk>/', views.GetCountryByID.as_view(),),
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('add_customer/', views.AddCustomer.as_view()),
]
