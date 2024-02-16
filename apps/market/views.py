from rest_framework import status
from rest_framework.response import Response

from apps.market.models import (
    Company,
    WorkTime,
    SocialNetwork,
    News
)

from apps.market.serializers import (
    CompanySerializer,
    UpdateCompanySerializer,
    WorkTimeSerializer,
    SocialSerializer,
    NewsSerializer,
    CreateNewsSerializer,
    UpdateNewsSerializer,
)

from rest_framework.generics import (
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    get_object_or_404,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    ListAPIView,
    CreateAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
)


class GetInfoCompanyGenericView(RetrieveAPIView):
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Company.objects.all()

    def get_object(self):
        return Company.objects.first()


class PutInfoCompanyGenericView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UpdateCompanySerializer

    def get_queryset(self):
        return Company.objects.all()

    def get_object(self):
        return Company.objects.first()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CompanySerializer(instance=instance)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request, *args, **kwargs):
        company = get_object_or_404(Company, id=1)

        serializer = self.get_serializer(instance=company, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class GetCreateWorkTimeGenericView(ListCreateAPIView):
    serializer_class = WorkTimeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        return WorkTime.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset:
            serializer = self.get_serializer(queryset, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )


class GetCreateSocialNetworkGenericView(ListCreateAPIView):
    serializer_class = SocialSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        return SocialNetwork.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset:
            serializer = self.get_serializer(instance=queryset, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )


class UpdateDeleteWorkTimeGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkTimeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        return WorkTime.objects.all()

    def get_object(self):
        instance_id = self.kwargs.get('id')
        return get_object_or_404(WorkTime, id=instance_id)


class UpdateDeleteSocialNetworkGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = SocialSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        return SocialNetwork.objects.all()

    def get_object(self):
        instance_id = self.kwargs.get('id')
        return get_object_or_404(SocialNetwork, id=instance_id)


class GetNewsGenericView(ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return News.objects.filter(date_deleted=None).all()

    def get(self, request, *args, **kwargs):
        instance = self.get_queryset()

        if instance:
            serializer = self.get_serializer(instance=instance, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )


class CreateNewsGenericView(CreateAPIView):
    serializer_class = CreateNewsSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return News.objects.all()

    def prepare_data(self):
        data = {
            'title': self.request.data['title'],
            'content': self.request.data['content'],
            'author': self.request.user.id
        }
        CreateNewsSerializer.Meta.fields.append('author')
        return data

    def post(self, request, *args, **kwargs):
        data = self.prepare_data()

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()

            CreateNewsSerializer.Meta.fields.remove('author')

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )


class UpdateDeleteNewsGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateNewsSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def get_queryset(self):
        return News.objects.all()

    def get_object(self):
        instance = News.objects.filter(id=self.kwargs['id_news']).first()
        return instance

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance:
            serializer = self.serializer_class(instance=instance)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def put(self, request, *args, **kwargs):
        instance = get_object_or_404(News, id=self.kwargs['id_news'])

        serializer = self.serializer_class(instance=instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(News, id=self.kwargs['id_news'])
        instance.delete()

        return Response(
            status=status.HTTP_200_OK,
            data="Deleted successfully"
        )
