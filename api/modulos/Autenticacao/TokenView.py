from .TokenSerializer import TokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer