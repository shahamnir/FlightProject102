from rest_framework import serializers
from .models import Custumer, Ticket
from AdminApp.models import User, UserRole
from AdminApp.serializers import UserSerializer
from AirlineApp.models import Flights


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Custumer
        fields = '__all__'

    """
    Uses create method to handle customer instance creation in order to create User instance when one created.
    """
    def create(self, validated_data):
        user_role = UserRole.objects.get(id=3)
        user = User.objects.create(
            user_role=user_role, username=validated_data['username'],
            email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        custumer = Custumer.objects.create(user=user, **validated_data)
        return custumer
    
  
class TicketSerializer(serializers.ModelSerializer):
    flight = serializers.PrimaryKeyRelatedField(queryset=Flights.objects.all())
    customer = serializers.PrimaryKeyRelatedField(
        queryset=Custumer.objects.all()
        )

    class Meta:
        model = Ticket
        fields = '__all__'
