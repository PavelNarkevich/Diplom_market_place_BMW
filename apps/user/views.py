from django.contrib.auth.models import User, Group
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
    ListAPIView,
    get_object_or_404,
)

from apps.user.models import Garage

from apps.staff.models import Chats, Message

from apps.user.errors_massages import NEW_PASSWORD_DO_NOT_MATCH_OLD_PASSWORD
from apps.user.serializers import (
    UserRegisterSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
    GarageSerializer,
    UpdateGarageSerializer,
    CreateQuestionSerializer,
    ChatsSerializer,
    UpdateChatMessagesSerializer
)


class UserRegisterGenericView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    @staticmethod
    def give_group_user(username):
        user = User.objects.filter(username=username).first()
        group = Group.objects.get(id=3)

        if group.name == 'Users':
            user.groups.add(3)  # Users group
            return user

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
                status=status.HTTP_205_RESET_CONTENT,
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
                    status=status.HTTP_205_RESET_CONTENT,
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


class GetUserGarageGenericView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GarageSerializer

    def get_queryset(self):
        return get_object_or_404(Garage, user=self.request.user.id)

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()

        serializer = self.serializer_class(instance=instance)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class UpdateUserGarageGenericView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateGarageSerializer

    def get_object(self):
        return get_object_or_404(Garage, user=self.request.user.id)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_205_RESET_CONTENT,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class CreateMessageGenericView(CreateAPIView):
    serializer_class = CreateQuestionSerializer
    permission_classes = [IsAuthenticated]

    def prepare_data(self):
        data = {
            **self.request.data,
            'user': self.request.user.id
        }
        self.serializer_class.Meta.fields.append('user')

        return data

    def post(self, request, *args, **kwargs):
        data = self.prepare_data()
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            serializer.Meta.fields.remove('user')

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        serializer.Meta.fields.remove('user')

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class GetUpdateMessageGenericView(RetrieveUpdateAPIView):
    serializer_class = UpdateChatMessagesSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return get_object_or_404(
            Chats,
            user_id=self.request.user.id,
            status='P' or 'Taken'
        )

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ChatsSerializer(instance=instance)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def prepare_data(self):
        data = {
            **self.request.data,
            'user': self.request.user.id
        }

        self.serializer_class.Meta.fields.append('user')

        return data

    def put(self, request, *args, **kwargs):
        data = self.prepare_data()

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.create(validated_data=serializer.validated_data)

            self.serializer_class.Meta.fields.remove('user')

            return Response(
                status=status.HTTP_205_RESET_CONTENT,
                data=serializer.data
            )

        self.serializer_class.Meta.fields.remove('user')

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )
