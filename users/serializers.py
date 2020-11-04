from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='image.file')
    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email', 'password', 'image')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data.get('username'), first_name=validated_data.get('first_name'),email= validated_data['email'],password = validated_data['password'])
        image = validated_data.pop('image')

        return user
