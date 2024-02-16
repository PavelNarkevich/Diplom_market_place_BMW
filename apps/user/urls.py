from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

from apps.user.views import (
    UserRegisterGenericView,
    GetUpdateProfileUserGenericView,
    UpdateUserPasswordGenericView,
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/register/', UserRegisterGenericView.as_view()),
    path("auth/refresh-token/", TokenRefreshView.as_view()),
    path('profile/', GetUpdateProfileUserGenericView.as_view()),
    path('profile/password/', UpdateUserPasswordGenericView.as_view()),
]