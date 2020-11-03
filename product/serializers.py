#from notify.models import Notification
from .models import Notifications
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ContactUs, Category, Post, Product, Order, Orderitems ,Notifications # , Cart


# for user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  #('img')
        """
        def create(self, validated_data):
            print('piccccccccccccccccccccccccccccccccccccccccc')
            print(validated_data)
            pic=Product(img=validated_data.get('pic'))
        """


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('fullname', 'email', 'description')

        # def create(self, validated_data):
        #     print('piccccccccccccccccccccccccccccccccccccccccc')
        #     print(validated_data)
        #     pic=abc(img=validated_data.get('pic'))

        def create(self, validated_data):
            print(validated_data)
            print(validated_data.get('fullname'))
            
            user = ContactUs.objects.create_user( fullname=validated_data.get('fullname'),email=validated_data.get('email'),description= validated_data['description'])
            # user = User.objects.create_user(first_name=validated_data.get('first_name'))

            return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderitems
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def update(self, instance, validated_data):
        order_obj = Order.objects.get(id=instance.id)
        data = { 'order_status':'Accepted'}
        order_updated_obj = OrderSerializer(order_obj, data=data)
        if order_updated_obj.is_valid():
            return
