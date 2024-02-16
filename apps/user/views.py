from django.contrib.auth.models import User
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)

from apps.user.errors_massages import NEW_PASSWORD_DO_NOT_MATCH_OLD_PASSWORD
from apps.user.serializers import (
    UserRegisterSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
)


class UserRegisterGenericView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer


    @staticmethod
    def give_group_user(username):
        user = User.objects.filter(username=username).first()

        user.groups.add(3)  # Users group
        return user

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            self.give_group_user(username=request.data["username"])

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class GetUpdateProfileUserGenericView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        user = self.request.user
        return user

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        if user:
            serializer = self.serializer_class(instance=user)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(instance=user, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class UpdateUserPasswordGenericView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        user = self.request.user
        return user

    def put(self, request, *args, **kwargs):
        user = self.get_object()

        if user.check_password(self.request.data['old_password']):
            serializer = self.serializer_class(instance=user, data=request.data)

            if serializer.is_valid(raise_exception=True):
                user.set_password(serializer.validated_data['password'])
                user.save()

                return Response(
                    status=status.HTTP_200_OK,
                    data="Password updated successfully"
                )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=NEW_PASSWORD_DO_NOT_MATCH_OLD_PASSWORD
        )
