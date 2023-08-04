from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response


"""
Function to get a user object by username and return its serialized data as a response.
"""
def get_user_by_username(request):
    username = request.data.get('username')
    user = User.objects.filter(username=username).first()
    serializer = UserSerializer(user)
    response = Response(serializer.data, status=200)
    return response
