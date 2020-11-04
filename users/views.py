from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.parsers import FileUploadParser
from product.models import *

"""login page"""


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
        if form.is_valid():
            template_name = 'user_registration/login.html'
            current_username = request.POST.get('username')
            current_password = request.POST.get('password')
            user = authenticate(username=current_username, password=current_password)
            request.session['username'] = user.username
            Specific_User = User.objects.get(username=current_username)
            totaldriver= len(Driver.objects.all())
            context = {
                'foo' : totaldriver
            }
            if user is not None:
                login(request, user)
                return render(request, 'examples/dashboard.html')
            else:
                print('User not found')
        else:
            context = {'LoginError': 'Please enter valid username or password'}
            return render(request, 'examples/pages/login.html', context)
    else:
        return render(request, 'examples/dashboard.html')


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        UserImage.objects.create(user_number=user, image=request.data.get('image'))
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
        return super(LoginAPI, self).post(request, format=None)


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'


@api_view(["POST"])
@permission_classes((AllowAny,))
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(
                {
                    "token": "logged in"
                },
                status=HTTP_200_OK)
        
        
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    names = request.data.get("name")
    username = request.data.get('username')
    password = request.data.get("password")
    address = request.data.get("address")
    all_fields = User._meta.get_fields()
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
