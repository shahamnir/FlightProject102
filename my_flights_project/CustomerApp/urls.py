from django.urls import path
from . import views

app_name = "customer_app"
urlpatterns = [
    path('create/',views.CustomerCreate.as_view(),name="customer_create"),
    path('list/',views.CustomerList.as_view(),name="customer_list"),
    path('details/<int:pk>/',views.CustomerDetails.as_view(),name="customer_details"),
    path('tickets/',views.TicketsList.as_view(),name="tickets_list"),
    path('tickets/<int:pk>/',views.TicketDetails.as_view(),name="ticket_details"),
    path('customer_by_username/',views.GetCustomerByUsername.as_view(),name="customer_by_username"),
    path('tickets_by_customer/',views.GetTicketsByCustomer.as_view(),name="tickets_by_customer"),

]