from django.urls import (
    path,
    include
)

urlpatterns = [
    path('catalog/', include('apps.catalog.urls')),
    path('company/', include('apps.market.urls')),
    path('users/', include('apps.user.urls')),
    path('staff/', include('apps.staff.urls'))
]
