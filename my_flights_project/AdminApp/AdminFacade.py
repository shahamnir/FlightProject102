from .models import User



def get_user_by_username(username):
    user = User.objects.filter(username)
    return user