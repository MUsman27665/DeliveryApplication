from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


"""class Category(models.Model):
    category_name = models.CharField(max_length=30, default="")
    # category_image =models.ImageField(upload_to='shopApp/images',default="shopApp/images/default.jpg")
    abc = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.category_name



class Product(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE) , 
    product_id = models.ForeignKey(to=Category, on_delete=models.CASCADE,related_name='product_id')
    product_name = models.CharField(max_length=30,default="")
    product_price = models.IntegerField(default="000")
    product_description = models.CharField(max_length=300, default="")
    product_image = models.ImageField(upload_to='iCV_Nation/images', default="iCV_Nation/images/defaults.jpg")
    category_type = models.CharField(max_length=30, default="")
    # user_pic =models.ImageField(upload_to='contacts/images',default="contacts/images/default.jpg")

    def __str__(self):
        return self.product_name


class abc(models.Model):
    img= models.ImageField(upload_to='iCV_Nation/images',default="iCV_Nation/images/defaults.jpg")

"""


class Driver(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    contact = models.CharField(max_length=14, default="0900")
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='iCV_Nation/images',default="iCV_Nation/images/defaults.jpg")
    # email=models.EmailField()
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics', storage=fs)

    def __str__(self):
        return "Driver "+self.firstname+" "+self.lastname
    # def delete(self, *args, **kwargs):
    #     self.profile_pics.delete()
    #     super().delete(*args, **kwargs)  # Call the "real" save() method.
    # def clean_firstname(self):
    #     firstname = self.cleaned_data['firstname']
    #     if firstname == 'a':
    #         print('raza')
    #         raise forms.ValidationError("please entefdddddddr first name")
    #     return firstname