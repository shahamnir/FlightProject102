from .models import Custumer, Ticket
from .serializers import CustomerSerializer, TicketSerializer
from rest_framework.response import Response


def get_customer_by_username(request):
    username = request.data.get('username')
    customer = Custumer.objects.filter(username=username).first()
    serializer = CustomerSerializer(customer)
    response = Response(serializer.data, status=200)
    return response


def get_tickets_by_customer(request):
    customer_id = request.data.get('customer_id')
    tickets = Ticket.objects.filter(customer_id=customer_id)
    serializer = TicketSerializer(tickets, many=True)
    response = Response(serializer.data, status=200)
    return response
    






