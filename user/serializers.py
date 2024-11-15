from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

# from core.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password' : {'write_only' : True, 'min_length' : 5}}

    def create(self, validated_data):
        '''Create User'''
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Validate and authenticate the user"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type' : 'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            self.context.get('request'),
            username = email,
            password = password
        )

        if not user:
            msg = 'Unable to authenticate with provided credentials.'
            raise serializers.ValidationError(msg, 'authorization')

        attrs['user'] = user
        return attrs