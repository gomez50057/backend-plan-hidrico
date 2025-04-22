from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginAPIView(APIView):
    """
    Autentica un usuario por username y password.
    Devuelve el/los grupo(s) al que pertenece.
    """
    authentication_classes = []  # Sin autenticación previa
    permission_classes = []      # Acceso libre

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            groups = list(user.groups.values_list('name', flat=True))
            return Response({
                'success': True,
                'groups': groups,
            })
        return Response(
            {'success': False, 'message': 'Credenciales inválidas'},
            status=status.HTTP_401_UNAUTHORIZED
        )