from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from .models import *



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('id', 'creates_at', 'updated_at')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()
        return instance


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    password1 = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'})

    def save_user(self, validated_data):
        password1 = validated_data.get('password1')
        password2 = validated_data.get('password2')
        if password1 != password2:
            raise ValidationError(detail={"password1": "Passwords dismatch"})
        else:
            user = User.objects.create_user(username=validated_data.get('username'), email=validated_data.get('email'),
                                            password=validated_data.get('password1'))
            token = Token.objects.create(user=user)
            return token.key

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
