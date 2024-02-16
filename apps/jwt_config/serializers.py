from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    AuthUser
)

from rest_framework_simplejwt.tokens import Token
from django.utils import timezone


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user=user)

        token['email'] = user.email
        token['user_name'] = user.username
        token['phone'] = user.phone

        user.last_login = timezone.now()
        user.save()

        return token
