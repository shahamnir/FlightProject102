from rest_framework import serializers
from .models import Airline, Country, Flights
from AdminApp.serializers import UserSerializer
from AdminApp.models import User, UserRole


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AirlineSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    country = serializers.SerializerMethodField()

    def get_country(self, obj):
        return obj.country.name

    class Meta:
        model = Airline
        fields = '__all__'

    """
    Uses create method to handle airline instance creation in order to create User instance when one created.
    """
    def create(self, validated_data):
        user_role = UserRole.objects.get(id=2)
        user = User.objects.create(
            user_role=user_role, username=validated_data['username'],
            email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        airline = Airline.objects.create(user=user, **validated_data)
        return airline


class FlightSerializer(serializers.ModelSerializer):
    airline = serializers.SerializerMethodField()
    origin_country = serializers.SerializerMethodField()
    destination_country = serializers.SerializerMethodField()

    def get_airline(self, obj):
        return obj.airline.name

    def get_origin_country(self, obj):
        return obj.origin_country.name

    def get_destination_country(self, obj):
        return obj.destination_country.name

    class Meta:
        model = Flights
        fields = '__all__'
            
    def validate(self, data):
        departure_time = data.get('departure_time')
        landing_time = data.get('landing_time')

        if landing_time < departure_time:
            raise serializers.ValidationError(
                "Landing time cannot be earlier than the departure time."
                )
        return data
        