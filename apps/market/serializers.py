from rest_framework import serializers

from apps.market.models import (
    Company,
    WorkTime,
    SocialNetwork,
    News,
)


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = ['id', 'day', 'time']


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['id', 'url', 'name']


class CompanySerializer(serializers.ModelSerializer):
    work_time = WorkTimeSerializer(many=True, read_only=True)
    social_network = SocialSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            'about_company',
            'address',
            'work_phone',
            'social_network',
            'work_time',
            'logo',
        ]


class UpdateCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'about_company',
            'address',
            'work_phone',
            'social_network',
            'work_time',
            'logo',
        ]


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = News
        fields = '__all__'


class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title',
            'content',
        ]


class UpdateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title',
            'content'
        ]
