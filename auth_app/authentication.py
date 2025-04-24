# auth_app/authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    """
    Permite extraer el JWT de la cookie 'access_token' si no llega por header.
    """
    def authenticate(self, request):
        # Primero intenta por header Authorization
        header = self.get_header(request)
        raw_token = None
        if header is not None:
            raw_token = self.get_raw_token(header)
        # Si no hay header, busca en cookies
        if raw_token is None:
            raw_token = request.COOKIES.get('access_token')
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token
