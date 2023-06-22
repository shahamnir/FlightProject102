from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from AdminApp.models import User
from .forms import RegisterForm


def home(request):
    return render(request, 'AnonymousApp/home.html')



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})




# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         address = request.POST['address']
#         phone_no = request.POST['phone_no']
#         credit_card_no = request.POST['credit_card_no']

#         user = User.objects.create_user(
#             username=username, password=password,
#             email=email, first_name=first_name,last_name=last_name,
#             address=address,phone_no=phone_no,credit_card_no=credit_card_no
#             )
#         user.save()
#         return redirect('login')

#     return render(request, 'registration.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return redirect('login')

#     return render(request, 'login.html')

# def user_logout(request):
#     logout(request)
#     return redirect('home')



