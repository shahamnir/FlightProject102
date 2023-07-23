from .models import Custumer, Ticket
from .serializers import CustomerSerializer, TicketSerializer
from rest_framework.response import Response


class CustomerFacade():
    def update_customer(request, pk):
        customer = Custumer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=200)
        else:
            response = Response(serializer.errors, status=400)
        return response
    
    def add_ticket(request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=201)
        else:
            response = Response(serializer.errors, status=400)
        return response
    
    def remove_ticket(request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        response = Response(status=200)
        return response
    
    def get_my_tickets(request):
        customer_id = request.data.get('customer_id')
        tickets = Ticket.objects.filter(customer_id=customer_id)
        serializer = TicketSerializer(tickets, many=True)
        response = Response(serializer.data, status=200)
        return response

