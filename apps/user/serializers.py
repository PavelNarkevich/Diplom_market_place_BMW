from django.contrib.auth import password_validation
from rest_framework import serializers

from django.contrib.auth.models import User
from apps.user.validators import ValidateRegisterData



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=32,
        min_length=8,
        write_only=True
    )
    password2 = serializers.CharField(
        max_length=32,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'password',
            'password2'
        ]

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def validate(self, attr):
        password = attr['password']
        password2 = attr['password2']
        phone = attr['phone']

        validate = ValidateRegisterData(password=password, password2=password2, phone=phone)

        validate.validate_pwd()
        validate.validate_phone()

        return attr

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
        )

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'phone',
            'first_name',
            'last_name',
            'email'
        ]


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=32, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=32, min_length=8, write_only=True)
    old_password = serializers.CharField(max_length=32, min_length=8, write_only=True)

    def validate(self, attr):
        password = attr['password']
        password2 = attr['password2']

        validate = ValidateRegisterData(password=password, password2=password2, phone=None)
        validate.validate_pwd()

        return attr