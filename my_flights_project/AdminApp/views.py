from .models import UserRole, User, Administrator
from .serializers import UserRoleSerializer, UserSerializer, AdministratorSerializer
from rest_framework.generics import (
    GenericAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView, CreateAPIView,ListAPIView
    )
from rest_framework.views import APIView
from rest_framework.response import Response
from .AdminFacade import get_user_by_username




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
    def get(self,request):
        username = request.data.get('username')
        user = get_user_by_username(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)