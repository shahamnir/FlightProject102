from .models import Custumer, Ticket




def get_customer_by_username(username):
    customer = Custumer.objects.filter(username=username).first()
    return customer

def get_tickets_by_customer(customer_id):
    ticket = Ticket.objects.filter(customer_id=customer_id)
    return ticket
    

