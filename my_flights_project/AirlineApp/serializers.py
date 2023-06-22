from rest_framework import serializers
from .models import Airline, Country, Flights
from AdminApp.serializers import UserSerializer
from AdminApp.models import User,UserRole

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AirlineSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = Airline
        # fields = ['username','password','email',
        #           'first_name', 'last_name', 'address', 'phone_no', 'credit_card_no','user']
        # extra_kwargs = {'user': {'required': False, "allow_null": True}}
        fields = '__all__'
        # exclude = ('user',)
    
    def create(self, validated_data):
        user_role = UserRole.objects.get(id=2)
        user = User.objects.create(
            user_role=user_role,username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        airline = Airline.objects.create(user=user, **validated_data)
        return airline
    
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'
    
    def validate(self, data):
        departure_time = data.get('departure_time')
        landing_time = data.get('landing_time')

        if landing_time < departure_time:
            raise serializers.ValidationError("Landing time cannot be earlier than the departure time.")

        return data
        