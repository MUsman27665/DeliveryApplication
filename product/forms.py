from django import forms
from .models import *
# from .validators import *

"""
class AddDriverForm(forms.ModelForm):
 
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    number = forms.IntegerField()
    address = forms.CharField(max_length=50)
    password1 = forms.CharField(max_length=30,min_length=8)
    password2 = forms.CharField(max_length=30,min_length=8)
    image = forms.ImageField(help_text='iCV_Nation/images')
    
    class Meta:
        model = Driver
        fields = '__all__'
"""
    # class Meta:
    #     model = User
    #     fields = ('first_name', 'username', 'address', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #         super(UserCreationForm, self).__init__(*args, **kwargs)
    #         for fieldname in ['password1', 'password2']:
    #             self.fields[fieldname].help_text = None

    #         x = self.fields['password1']
    #         x.label = "Password:"
    #         y = self.fields['password2']
    #         y.label = "Confirm Password:"

    #         z.label = ""

"""
def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
        raise forms.ValidationError("Password & Confirm Password are not same.")
    return password2
"""
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.username = self.cleaned_data['username']
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user


class createPostForm(forms.ModelForm):

    title = forms.CharField(max_length=50,label='post_title', widget=forms.TextInput(attrs={'placeholder': '  Enter Title Here','class':'form-control input-border-bottom rounded-0 p-0'}))
    description = forms.CharField(max_length=200, label='post_description', widget=forms.TextInput(attrs={'placeholder': '  Enter description here','class':'form-control input-border-bottom rounded-0 p-0'}))
    image = forms.ImageField(help_text='iCV_Nation/images', label='post_image', widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = Post
        fields = {'title','description','image'}


class addCategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=50, label='category_name', widget=forms.TextInput(attrs={'placeholder': '  Enter Title Here','class':'form-control input-border-bottom rounded-0 p-0'}))
    # description = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': '  Enter description here','class':'form-control input-border-bottom rounded-0 p-0'}))
    image = forms.ImageField(help_text='iCV_Nation/category', label='category_image', widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = Category
        fields = '__all__'

class addProductForm(forms.ModelForm):
    # product_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': '  Enter Title Here','class':'form-control input-border-bottom rounded-0 p-0'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),label='category_id')
    product_name = forms.CharField(max_length=30,label='product_name',widget=forms.TextInput(attrs={'placeholder': '  Enter product name Here','class':'form-control input-border-bottom rounded-0 p-0'}))
    product_price = forms.IntegerField(label='product_price')
    product_description = forms.CharField(label='product_description',widget=forms.Textarea(attrs={"rows":5, "cols":60,'placeholder': '  Enter product description here','class':'form-control input-border-bottom rounded-0 p-0'}))
    product_image = forms.ImageField(label='product_image',help_text='iCV_Nation/product',widget=forms.FileInput(attrs={'class':'form-control-file'}))



    # product_id = models.ForeignKey(to = Category, on_delete=models.CASCADE,related_name='product_id')
    # product_name = models.CharField(max_length=30,default="")
    # product_price = models.IntegerField(default="000")
    # product_description = models.CharField(max_length=300,default="")
    # product_image =models.ImageField(upload_to='iCV_Nation/product',default="iCV_Nation/images/defaults.jpg")
    # category_type = models.CharField(max_length=30,default="")
    class Meta:
        model = Product
        fields = {'category', 'product_name', 'product_price', 'product_description','product_image'}