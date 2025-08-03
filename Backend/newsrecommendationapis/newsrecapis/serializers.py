from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    #confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password',  
            'name', 
            'phone_number', 
            'preferred_news_categories'
        ]

    def validate(self, data):
        # Ensure password and confirm_password match
        return data

    def create(self, validated_data):
        # Remove confirm_password as it's not used in user creation
        password = validated_data.pop('password')

        # Create and save the user
        user = User(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'phone_number', 'preferred_news_categories']
        read_only_fields = ['id', 'username', 'email'] 