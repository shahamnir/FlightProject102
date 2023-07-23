from django.urls import path
from . import views

app_name = "customer_app"
urlpatterns = [
    path('create/', views.CustomerCreate.as_view(),),
    path('list/', views.CustomerList.as_view(),),
    path('details/<int:pk>/', views.CustomerDetails.as_view(),),
    path('tickets/', views.TicketsList.as_view(),),
    path('tickets/<int:pk>/', views.TicketDetails.as_view(),),
    path('customer_by_username/', views.GetCustomerByUsername.as_view(),),
    path('tickets_by_customer/', views.GetTicketsByCustomer.as_view(),),
    path('details_customer/<int:pk>/', views.DetailsCustomer.as_view(),),
    path('add_ticket/', views.AddTicket.as_view(),),
    path('details_ticket/<int:pk>/', views.DetailsTicket.as_view(),),
    path('my_tickets/', views.GetMyTickets.as_view(),),

]
