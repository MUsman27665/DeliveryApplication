from django.shortcuts import render, redirect
import json
#for rest api
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import *
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from iCV_Nation import settings
from users.forms import SignUpForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from users.models import *
import requests
from users.forms import *

from .models import *
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer #,ProductSerializer

from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
#for rest_image
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from PIL import Image
#for email
from django.core.mail import send_mail

from product.models import *


@csrf_exempt
# @login_required
def addDriver(request):
    if request.method == 'POST' and request.FILES['image']:
        print(request.user)
        # print(request.FILES['image'])
        print(request.POST['last_name'])
        print(request.POST['password'])
        print(request.POST['confirm_password'])
        print(request.FILES['image'])
        # image_source ='contacts/images/'+request.POST['image']

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password and confirm_password:
            if password != confirm_password:
                context = {'LoginError': 'Please enter credentials'}
                raise forms.ValidationError("The two password fields must match.")
            else:
                Driver.objects.create(
                    firstname=request.POST['first_name'],
                    lastname=request.POST['last_name'],
                    email=request.POST['email'],
                    contact=request.POST['number'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    image=request.FILES['image']
                )

        return redirect('loggedin')

    else:

        return render(request, 'examples/adddriver.html')

    # if request.method=='POST':
    #     myform = AddDriverForm(request.POST,request.FILES)
    #     print(request.POST)
    #     if myform.is_valid():
    #         print("pic")

    #         myform.save()
    #         return redirect('loggedin')
    #     else:
    #         print(myform.errors)
    #         context = {
    #             'myform':myform
    #         }
    #         return render(request,'examples/adddriver.html', context)
    # else:
    #     myform=AddDriverForm()
    #     print(myform.errors)
    #     print('this is get')
    #     return render(request,'examples/adddriver.html',{'myform':myform})


def showDrivers(request):
    all_drivers = Driver.objects.all()
    print(all_drivers)

    #print("", settings.MEDIA_ROOT)

    image_source = settings.SERVER_URL + '/media/'

    context = {
        'drivers': all_drivers,
        'image_source': image_source
    }

    return render(request, 'examples/showDriver.html', context)


@csrf_exempt
def updateDriver(request, userid):
    if request.method == 'POST':
        print('helooooooooooooooooooooooooooooo')
        drive = Driver.objects.get(id=userid)
        print(drive)

        if (request.POST['firstname'] is not None and request.POST['lastname'] is not None):

            print("Pic is coming.......")
            drive.firstname = request.POST['firstname']
            drive.lastname = request.POST['lastname']
            drive.address = request.POST['address']
            print('99999999999999999999999999999999')
            print('99999999999999999999999999999999')

            # if (request.POST['image'] is None):
            # profile_pics    = request.FILES['image']
            # drive.image = profile_pics

            image_path = 'media/contacts/'
            # pic =image_path + profile_pics
            # image_path = 'media/contacts/images'+profile_pics
            # image_path      = profile_pics.url

            # user = {}
            # user.firstname = "asim"
            # user.lastname = "azhar"
            # user.gender = "male"
            # user.password = "male"

            # jsonuser = json.loads(user)

            drive.save()
            return redirect('loggedin')
        else:
            print("pic is not coming........")
            user_id = Driver.objects.get(id=userid)
            return render(request, 'examples/updateDriver.html', {'obj': user_id})
    else:
        obj = Driver.objects.get(id=userid)
        return render(request, 'examples/updateDriver.html', {'obj': obj})


@csrf_exempt
def deleteDriver(request, id):
    # if request.method=='POST':
    #     obj=StudentForm(request.POST,request.FILES)

    #     Student.objects.get(id=id).delete()
    #     return redirect('/')
    # else:
    print('wowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
    drive = Driver.objects.get(id=id).delete()
    return redirect('../showDrivers/')


#login page
@csrf_exempt
def loginPage(request):

    return render(request, "examples/pages/login.html")

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')

@csrf_exempt
def loggedin(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print('khan g')
        if form.is_valid():
            template_name = 'user_registration/login.html'
            current_username = request.POST.get('username')
            current_password = request.POST.get('password')
            user = authenticate(username = current_username, password = current_password)
            # user = form.get_user()
            request.session['username'] = user.username
            print(user)
            Specific_User = User.objects.get(username=current_username)
            totaldriver= len(Driver.objects.all())
            print('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            print(totaldriver)
            context = {
                'foo' : totaldriver
            }

            print(Specific_User)
            if user is not None:
                print(user)
                login(request, user)
                return render(request, 'examples/dashboard.html')
            else:
                print('User not found')
            # return redirect('users:verifycode')
            
        else:
            context= {'LoginError': 'Please enter valid username or password'}
            return render(request, 'examples/pages/login.html', context)
    else:
        
        return render(request, 'examples/dashboard.html')

# @csrf_exempt
# def addDriver(request):
#     if request.method == 'POST':
#         print(request.POST['image'])
#         # print(request.POST['last_name'])
#         print(request.POST['password'])
#         print(request.POST['confirm_password'])

#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         if password and confirm_password:
#             if password != confirm_password:
#                 context= {'LoginError': 'Please enter credentials'}
#                 raise forms.ValidationError("The two password fields must match.")
#             else:
#                 Driver.objects.create(
#                     firstname = request.POST['first_name'],
#                     lastname  = request.POST['last_name'],
#                     email     = request.POST['email'],
#                     contact   = request.POST['number'],
#                     address   = request.POST['address'],
#                     password  = request.POST['password'],
#                     image     = request.POST['image']
#                 )
        
        
        
#         return redirect('loggedin')

#     else:

#         return render(request, 'examples/adddriver.html')


# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        print(request.user)
        return super(LoginAPI, self).post(request, format=None)


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'

"""
class addProduct(APIView):
    parser_class = (ImageUploadParser,)
    def post(self, request, format=None):
        print('-----------------------------------------')
        
        print(request.user)
        
        x = Category.objects.get(category_name='car')
        
        Product.objects.create( 
            product_name = request.data['name'],
            product_price = request.data['price'],
            product_description = request.data['description'],
            product_image = request.data['pic'],
            category_type = request.data['type'],
            product_id=x
        )
        # return Response(status=status.HTTP_201_CREATED)        
        
        return Response(
            {
                'Msg': 'Product successfully added'
            },
            status=HTTP_200_OK)




class addCategory(APIView):
    parser_class = (ImageUploadParser,)
    def post(self, request, format=None):
        print('-----------------------------------------')
        
        print(self.request.user)
        
        # Product.objects.create(product_name=request.data['name'],product_price=request.data['price'],product_description=request.data['description'],product_image=request.data['pic'],category_type=request.data['type'])
        # x=Product(product_name=request.data['name'],product_price=request.data['price'],product_description=request.data['description'],product_image=request.data['pic'],category_type=request.data['type'])
        # x.save()
        # Category.objects.create(category_name='electric',abc='abc')
        x= Category.objects.create(
            category_name=request.data['category_name'],
            abc = request.data['abc']
        )
        # Product.objects.create(email="vale@vale.io", user=product_id)
        
        
        # return Response(status=status.HTTP_201_CREATED)        
        
        return Response(
            {
                'Msg': 'Product successfully added'
            },
            status=HTTP_200_OK)
"""

@api_view(["POST"])
@permission_classes((AllowAny,))
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if request.method == "POST":
        # if login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user: 
            print('heloo')
            login(request, user)
            return Response(
                {
                    "token": "logged in"
                },
                status=HTTP_200_OK)
            # do something or redirect
    # print(request.data)
    # if username is None or password is None:
    #     return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
    # user = authenticate(username=username,password=password)
    # print(user)
    # if not user:
    #     return Response({'Msg': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
    # userObj = User.objects.get(username=user)
    # token = Token.objects.get_or_create(user=userObj)

    # token = token.key
        
    
        
        
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    names = request.data.get("name")
    username = request.data.get('username')
    password = request.data.get("password")
    address= request.data.get("address")
    all_fields=User._meta.get_fields()
    print(all_fields)
    if names is None or address is None or password is None or username is None:
        return Response({'Msg': ''},status=HTTP_400_BAD_REQUEST)
    user = User.objects.filter(username=username)
    if user:
        
        return Response({'Msg': 'Exists'},status=HTTP_406_NOT_ACCEPTABLE)

    if not user:
        user_obj = User(name=names,username=username,address = address)
        user_obj.set_password(password)
        user_obj.save()
        
    return Response({'Msg': 'created','token': 'token'},status=HTTP_200_OK)
    


        