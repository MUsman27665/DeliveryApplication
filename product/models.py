from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


class Driver(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,blank=True,unique=True)
    contact = models.CharField(max_length=14, default="0900",unique=True)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='iCV_Nation/images',default="iCV_Nation/images/defaults.jpg")

    def __str__(self):
        return self.firstname+" "+self.lastname


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    Date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='iCV_Nation/post',blank=True,null =True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    category_name = models.CharField(max_length=30,default="")
    category_image = models.ImageField(upload_to='iCV_Nation/category',default="")

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    product_name = models.CharField(max_length=30, default="")
    product_price = models.IntegerField(default="000")
    product_description = models.CharField(max_length=300, default="")
    product_image = models.ImageField(upload_to='iCV_Nation/images', default="iCV_Nation/images/defaults.jpg")

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_status_choice = [
        ('I', 'Initiated'),
        ('A', 'Accepted'),
        ('CBD', 'Canceled By Driver'),
        ('D', 'Delivered'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id', null=True)
    order_number = models.IntegerField(default=000, unique=True)
    total_products = models.IntegerField(default=000)
    total_cost = models.DecimalField(default=000, decimal_places=2, max_digits=5)
    shipping_address = models.CharField(max_length=300, default='user location')
    additional_requirements = models.TextField(default='additional_requirements')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default=1)
    order_status = models.CharField(choices=order_status_choice, max_length=200, default='Initiated')
    order_date = models.DateField(default=2020-11)

    def __str__(self):
        return self.order_number


class Orderitems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userid', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id',default=1)
    product_quantity = models.IntegerField(default=000)
    product_cost_total = models.IntegerField(default=000)
    order_number = models.IntegerField(default=000)

    def __str__(self):
        return self.order_number


class Notifications(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default=1)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, default=3)
    message = models.CharField(max_length=200, default='message')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.message


class UserImage(models.Model):
    user_number = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='iCV_Nation/images', default="iCV_Nation/images/defaults.jpg")