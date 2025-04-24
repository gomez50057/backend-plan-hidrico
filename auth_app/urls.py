from django.urls import path
from .views import LoginAPIView, RefreshAPIView, LogoutAPIView, MeAPIView

urlpatterns = [
    path('login/',   LoginAPIView.as_view(),   name='api-login'),
    path('refresh/', RefreshAPIView.as_view(), name='api-refresh'),
    path('logout/',  LogoutAPIView.as_view(),  name='api-logout'),
    path('me/',      MeAPIView.as_view(),      name='api-me'),
]