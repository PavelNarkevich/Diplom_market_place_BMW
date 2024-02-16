from django.contrib import admin
from apps.market.models import (
    SocialNetwork,
    WorkTime,
    Company,
)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')


@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    list_display = ('day', 'time')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'about_company',
        'address',
        'work_phone',
        'logo'
    )
