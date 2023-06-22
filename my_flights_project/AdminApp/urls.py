from django.urls import path
from . import views

app_name = "admin_app"
urlpatterns = [
    path('user_roles/',views.UserRoles.as_view(),name="user_roles"),
    path('user_role/<int:pk>/',views.UserRoleDetails.as_view(),name="user_role"),
    path('users/',views.Users.as_view(),name="users"),
    path('users/<int:pk>',views.UserDetails.as_view(),name="user_details"),
    path('list/',views.AdministratorsList.as_view(),name="administrators_list"),
    path('create/',views.AdministratorCreate.as_view(),name="administrator_create"),
    path('details/<int:pk>/',views.AdministratorDetails.as_view(),name="administrator_details"),
    path('get_user_by_username/',views.GetUserByUsername.as_view(),name="get_user_by_username"),
]