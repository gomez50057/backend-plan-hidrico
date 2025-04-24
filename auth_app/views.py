from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if not user:
            return Response({'detail': 'Credenciales inválidas'}, status=401)

        refresh = RefreshToken.for_user(user)
        # Inyecta grupos en el token
        refresh['groups'] = list(user.groups.values_list('name', flat=True))
        access_token = str(refresh.access_token)

        resp = Response({'access': access_token})
        # Cookies HTTP-Only
        resp.set_cookie(
            'access_token', access_token,
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Strict',
            max_age=15*60,
            path='/'  # válida para todo tu dominio
        )
        resp.set_cookie(
            'refresh_token', str(refresh),
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Strict',
            max_age=7*24*3600,
            path='/'  
        )
        return resp

class RefreshAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        token = request.COOKIES.get('refresh_token')
        if not token:
            return Response({'detail': 'Sin refresh token'}, status=401)
        try:
            refresh = RefreshToken(token)
            new_access = str(refresh.access_token)
            resp = Response({'access': new_access})
            resp.set_cookie('access_token', new_access,
                            httponly=True, secure=not settings.DEBUG,
                            samesite='Strict', max_age=15*60, path='/')
            return resp
        except Exception:
            return Response({'detail': 'Refresh inválido'}, status=401)

class LogoutAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        resp = Response({'detail': 'Logged out'})
        resp.delete_cookie('access_token', path='/')
        resp.delete_cookie('refresh_token', path='/')
        return resp