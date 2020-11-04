from rest_framework import serializers
from .models import ContactUs, Category, Post, Order, Orderitems ,Notifications, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('fullname', 'email', 'description')

        def create(self, validated_data):
            user = ContactUs.objects.create_user( fullname=validated_data.get('fullname'),email=validated_data.get('email'),description= validated_data['description'])
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
        data = {'order_status': 'Accepted'}
        order_updated_obj = OrderSerializer(order_obj, data=data)
        if order_updated_obj.is_valid():
            return
