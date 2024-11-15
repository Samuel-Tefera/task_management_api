from django.contrib.auth import get_user_model

from rest_framework import (
    generics,
    authentication,
    permissions
    )
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers


class CreateUSerView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = serializers.UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new token for a user."""
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticat user"""
    serializer_class = serializers.UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user