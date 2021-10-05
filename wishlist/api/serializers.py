from rest_framework import serializers
from users.models import *
from home.models import *
from items.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'firstname', 'lastname']

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'firstname', 'lastname']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User (
            username=self.validated_data.get('username', ''),
            firstname=self.validated_data.get('firstname', ''),
            lastname=self.validated_data.get('lastname', ''),
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.password=password
        user.save()
        return user

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'