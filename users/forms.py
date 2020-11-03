from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# class SignUpForm(UserCreationForm):
from users.models import Driver


class AddDriverForm(forms.ModelForm):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    number = forms.IntegerField()
    address = forms.CharField(max_length=50)
    password1 = forms.CharField(max_length=30, min_length=8)
    password2 = forms.CharField(max_length=30, min_length=8)
    image = forms.ImageField(help_text='iCV_Nation/images')

    class Meta:
        model = Driver
        fields = '__all__'


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    password1 = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'address', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            for fieldname in ['password1', 'password2']:
                self.fields[fieldname].help_text = None

            x = self.fields['password1']
            x.label = "Password:"
            y = self.fields['password2']
            y.label = "Confirm Password:"

            z.label = ""

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password & Confirm Password are not same.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user