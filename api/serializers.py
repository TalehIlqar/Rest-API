import random
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from user.models import User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "email",
                  "phone_number", "password", 'password_confirmation')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    password_confirmation = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                {'password': 'Password does not match.'})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        random_number = random.randint(0, 10000)
        while User.objects.filter(username=f"Guest_{random_number}"):
            random_number = random.randint(0, 1000000)
        validated_data['username'] = f"Guest_{random_number}"
        user = super().create(validated_data=validated_data)
        user.set_password(password)
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
