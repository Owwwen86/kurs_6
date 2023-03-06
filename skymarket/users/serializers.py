from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
        )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        auth_user = User.objects.create_user(**validated_data)
        auth_user.is_active = True
        if password is not None:
            # Set password does the hash, so you don't need to call make_password
            auth_user.set_password(password)
        auth_user.save()
        return auth_user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "image", ]


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "id", "email", "image", ]

