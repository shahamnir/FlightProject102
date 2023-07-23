from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from rest_framework.views import APIView
from .FacadeBase import FacadeBase
from rest_framework.response import Response


class GetAllFlights(APIView):
    def get(self, request):
        response = FacadeBase.get_all_flights(request)
        return response


class GetFlightByID(APIView):
    def get(self, request, pk):
        response = FacadeBase.get_flight_by_id(request=request, pk=pk)
        return response


class GetFlightsByParams(APIView):
    def get(self, request):
        response = FacadeBase.get_flights_by_params(request)
        return response


class GetAllAirlines(APIView):
    def get(self, request):
        response = FacadeBase.get_all_airlines(request)
        return response


class GetAirlineByID(APIView):
    def get(self, request, pk):
        response = FacadeBase.get_airline_by_id(request=request, pk=pk)
        return response


class GetAirlineByParams(APIView):
    def get(self, request):
        response = FacadeBase.get_airline_by_params(request)
        return response


class GetAllCountries(APIView):
    def get(self, request):
        response = FacadeBase.get_all_countries(request)
        return response


class GetCountryByID(APIView):
    def get(self, request, pk):
        response = FacadeBase.get_country_by_id(request=request, pk=pk)
        return response


class AddCustomer(APIView):
    def post(self, request):
        response = FacadeBase.add_customer(request)
        return response


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})

        else:
            return Response({'message': 'Invalid credentials'}, status=400)


class RegisterView(APIView):
    def post(self, request):
        response = FacadeBase.register(request)
        return response


def home(request):
    return render(request, 'AnonymousApp/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
