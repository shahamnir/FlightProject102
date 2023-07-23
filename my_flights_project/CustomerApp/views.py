from .models import Custumer, Ticket
from .serializers import CustomerSerializer, TicketSerializer
from rest_framework.generics import (
    ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
)
from rest_framework.views import APIView
from .CustomerFunctions import (
    get_customer_by_username, get_tickets_by_customer
)
from .CustomerFacade import CustomerFacade


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
    def get(self, request):
        response = get_customer_by_username(request)
        return response


class GetTicketsByCustomer(APIView):
    def get(self, request):
        response = get_tickets_by_customer(request)
        return response


class DetailsCustomer(APIView):
    def put(self, request, pk):
        response = CustomerFacade.update_customer(request, pk)
        return response


class AddTicket(APIView):
    def post(self, request):
        response = CustomerFacade.add_ticket(request)
        return response


class DetailsTicket(APIView):
    def delete(self, request, pk):
        response = CustomerFacade.remove_ticket(request, pk)
        return response


class GetMyTickets(APIView):
    def get(self, request):
        response = CustomerFacade.get_my_tickets(request)
        return response

    