from rest_framework import serializers
from .models import User, UserRole, Administrator


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'user_role']


class AdministratorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Administrator
        fields = '__all__'

    def create(self, validated_data):
        user_role = UserRole.objects.get(id=1)
        user = User.objects.create(
            user_role=user_role,
            username=validated_data['username'],
            email=validated_data['email'],
            is_superuser=True,
            is_staff=True
            )
        user.set_password(validated_data['password'])
        user.save()
        administrator = Administrator.objects.create(user=user,
                                                     **validated_data)
        return administrator
