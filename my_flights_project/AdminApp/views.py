from .models import UserRole, User, Administrator
from .serializers import (
    UserRoleSerializer, UserSerializer, AdministratorSerializer
    )
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView, ListAPIView
    )
from rest_framework.views import APIView
from .AdminFunctions import get_user_by_username
from .AdminFacade import AdminFacade


class UserRoles(ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class UserRoleDetails(RetrieveUpdateDestroyAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class Users(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdministratorsList(ListAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class AdministratorCreate(CreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class AdministratorDetails(RetrieveUpdateDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class GetUserByUsername(APIView):
    def get(self, request):
        response = get_user_by_username(request)
        return response


class GetAllCustomers(APIView):
    def get(self, request):
        response = AdminFacade.get_all_customers(request)
        return response

  
class AddAirline(APIView):
    def post(self, request):
        response = AdminFacade.add_airline(request)
        return response


class RemoveAirline(APIView):
    def delete(self, request, pk):
        response = AdminFacade.remove_airline(request, pk)
        return response


class AddCustomer(APIView):
    def post(self, request):
        response = AdminFacade.add_customer(request)
        return response
    

class AddAdministrator(APIView):
    def post(self, request):
        response = AdminFacade.add_administrator(request)
        return response


class RemoveCustomer(APIView):
    def delete(self, request, pk):
        response = AdminFacade.remove_customer(request, pk)
        return response
    

class RemoveAdministrator(APIView):
    def delete(self, request, pk):
        response = AdminFacade.remove_administrator(request, pk)
        return response
