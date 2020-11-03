from rest_framework import serializers
from django.contrib.auth.models import User
#from .models import abc, Category, Product


# from django.contrib.auth import get_user_model

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id','username','first_name', 'email')
        fields = '__all__'

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','username', 'email', 'password')
        # fields = ('id','first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print('validated_data')
        print(validated_data.get('first_name'))
        
        user = User.objects.create_user( username=validated_data.get('username'),first_name=validated_data.get('first_name'),email= validated_data['email'],password = validated_data['password'] )
        # user = User.objects.create_user(first_name=validated_data.get('first_name'))

        return user

# for product

"""
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = abc
        fields = '__all__' #('img')

        def create(self, validated_data):
            print('piccccccccccccccccccccccccccccccccccccccccc')
            print(validated_data)
            pic=abc(img=validated_data.get('pic'))
            
"""





