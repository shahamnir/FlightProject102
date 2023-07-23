from django.urls import path
from . import views

app_name = "admin_app"
urlpatterns = [
    path('user_roles/', views.UserRoles.as_view(),),
    path('user_role/<int:pk>/', views.UserRoleDetails.as_view(),),
    path('users/', views.Users.as_view(),),
    path('users/<int:pk>', views.UserDetails.as_view()),
    path('list/', views.AdministratorsList.as_view(),),
    path('create/', views.AdministratorCreate.as_view(),),
    path('details/<int:pk>/', views.AdministratorDetails.as_view(),),
    path('get_user_by_username/', views.GetUserByUsername.as_view(),),
    path('all_customers/', views.GetAllCustomers.as_view(),),
    path('add_airline/', views.AddAirline.as_view(),),
    path('remove_airline/<int:pk>/', views.RemoveAirline.as_view(),),
    path('add_customer/', views.AddCustomer.as_view(),),
    path('add_administrator/', views.AddAdministrator.as_view(),),
    path('remove_customer/<int:pk>/', views.RemoveCustomer.as_view(),),
    path('remove_administrator/<int:pk>/', views.RemoveAdministrator.as_view())
]
