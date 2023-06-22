from .models import Custumer, Ticket
from .serializers import CustomerSerializer, TicketSerializer
from rest_framework.generics import (
    ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView, CreateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .CustomerFacade import get_customer_by_username, get_tickets_by_customer



class CustomerList(ListAPIView):
    queryset = Custumer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreate(CreateAPIView):
    queryset = Custumer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetails(RetrieveUpdateDestroyAPIView):
    queryset = Custumer.objects.all()
    serializer_class = CustomerSerializer

class TicketsList(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetails(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class GetCustomerByUsername(APIView):
    def get(self,request):
        username = request.data.get('username')
        customer = get_customer_by_username(username=username)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=200)

class GetTicketsByCustomer(APIView):
    def get(self,request):
        customer_id = request.data.get('customer_id')
        tickets = Ticket.objects.filter(customer_id=customer_id)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data,status=200)
    