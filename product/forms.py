from django import forms
from .models import *


class createPostForm(forms.ModelForm):
    title = forms.CharField(max_length=50,label='post_title', widget=forms.TextInput(attrs={'placeholder': '  Enter Title Here','class':'form-control input-border-bottom rounded-0 p-0'}))
    description = forms.CharField(max_length=200, label='post_description', widget=forms.TextInput(attrs={'placeholder': '  Enter description here','class':'form-control input-border-bottom rounded-0 p-0'}))
    image = forms.ImageField(help_text='iCV_Nation/images', label='post_image', widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = Post
        fields = {'title','description','image'}


class addCategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=50, label='category_name', widget=forms.TextInput(attrs={'placeholder': '  Enter Title Here','class':'form-control input-border-bottom rounded-0 p-0'}))
    image = forms.ImageField(help_text='iCV_Nation/category', label='category_image', widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = Category
        fields = '__all__'


class addProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),label='category_id')
    product_name = forms.CharField(max_length=30,label='product_name',widget=forms.TextInput(attrs={'placeholder': '  Enter product name Here','class':'form-control input-border-bottom rounded-0 p-0'}))
    product_price = forms.IntegerField(label='product_price')
    product_description = forms.CharField(label='product_description',widget=forms.Textarea(attrs={"rows":5, "cols":60,'placeholder': '  Enter product description here','class':'form-control input-border-bottom rounded-0 p-0'}))
    product_image = forms.ImageField(label='product_image',help_text='iCV_Nation/product',widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = Product
        fields = {'category', 'product_name', 'product_price', 'product_description','product_image'}
