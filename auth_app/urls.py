# auth_app/urls.py
from django.urls import path
from .views import LoginAPIView, RefreshAPIView, LogoutAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='api-login-slash'),
    # path('login',  LoginAPIView.as_view(), name='api-login'),
    path('refresh/', RefreshAPIView.as_view(), name='api-refresh'),
    path('logout/',  LogoutAPIView.as_view(), name='api-logout'),
]