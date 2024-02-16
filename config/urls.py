from django.contrib import admin
from django.urls import (
    path,
    include,
    re_path
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    info=openapi.Info(
        title="Diplom api documentation",
        default_version='v1',
        description="Marketplace API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="XuiVam@mail.ru"),
        license=openapi.License(name="QWERTY"),
    ),
    public=True,
    permission_classes=([AllowAny])
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.router')),
    re_path(
        r"^swagger(?P<format>\.yaml|\.json)$",
        schema_view.without_ui(cache_timeout=0),
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0)
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0)
    )
]
