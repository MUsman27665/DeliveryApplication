from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from .serializers import ContactUsSerializer, CategorySerializer, PostSerializer, ProductSerializer, OrderSerializer, \
    OrderItemsSerializer, NotificationSerializer
from rest_framework import generics, permissions
from django.core.mail import send_mail
from .models import Notifications

@csrf_exempt
def addDriver(request):
    if request.method == 'POST' and request.FILES['image']:
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


def showDrivers(request):
    all_drivers = Driver.objects.all()
    image_source = settings.SERVER_URL + '/media/'
    context = {
        'drivers': all_drivers,
        'image_source': image_source
    }
    return render(request, 'examples/showDriver.html', context)


@csrf_exempt
def updateDriver(request, userid):
    if request.method == 'POST':
        drive = Driver.objects.get(id=userid)
        if request.POST['firstname'] is not None and request.POST['lastname'] is not None:
            drive.firstname = request.POST['firstname']
            drive.lastname = request.POST['lastname']
            drive.address = request.POST['address']
            image_path = 'media/contacts/'
            drive.save()
            return redirect('loggedin')
        else:
            user_id = Driver.objects.get(id=userid)
            return render(request, 'examples/updateDriver.html', {'obj': user_id})
    else:
        obj = Driver.objects.get(id=userid)
        return render(request, 'examples/updateDriver.html', {'obj': obj})


@csrf_exempt
def deleteDriver(request, id):
    drive = Driver.objects.get(id=id).delete()
    return redirect('../showDrivers/')


@csrf_exempt
def createPost(request):
    if request.method=='POST':
        myform = createPostForm(request.POST,request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('../loggedin/')
        else:
            context = {
                'myform': myform
            }
            return render(request, 'examples/createPost.html', context)
    else:
        myform = createPostForm()
        return render(request, 'examples/createPost.html', {'myform':myform})


def displayCategories(request):
    all_category = Category.objects.all()
    image_source = settings.SERVER_URL + '/media/'
    context = {
        'category': all_category,
        'image_source': image_source
    }
    return render(request, 'examples/displayCategory.html', context)


# Adding Products
@csrf_exempt
def addProducts(request):
    # print(self.request.user)
    if request.method == 'POST':
        myform = addProductForm(request.POST, request.FILES)
        print(request.POST)
        if myform.is_valid():
            print(myform)
            myform.save()
            return redirect('loggedin')
        else:
            context = {
                'myform': myform
            }
            return render(request, 'examples/addProducts.html', context)
    else:
        myform = addProductForm()
        return render(request, 'examples/addProducts.html', {'myform': myform})


def displayProducts(request):
    all_products = Product.objects.all()
    image_source = settings.SERVER_URL + '/media/'
    context = {
        'products': all_products,
        'image_source': image_source
    }
    return render(request, 'examples/displayProducts.html', context)


def displayPost(request):
    all_posts = Post.objects.all()
    image_source = settings.SERVER_URL+'/media/'
    print(image_source)
    context= {
            'posts': all_posts,
            'image_source': image_source
    }
    return render(request, 'examples/displayPost.html', context)


def deletePost(request,id):
    drive = Post.objects.get(id=id).delete()
    return redirect('../displayPost/')


class contactUs(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContactUsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                'Msg': 'Product successfully added'
            },
            status=HTTP_200_OK)


def displayQuery(request):
    all_queries = ContactUs.objects.all()
    context={
        'all_queries': all_queries
    }
    return render(request, 'examples/displayQuery.html',context)


# @csrf_exempt
def sendmail(request, id):
    subject = request.data.get('subject')
    body = request.data.get('body')
    email = request.data.get('email')
    contact = ContactUs.objects.get(id=id)
    if request.method=='POST':
        subject = request.POST['subject']
        body = request.POST['body']
        email = contact.email
        msg=send_mail(subject,body,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        return redirect('../displayQuery')
    else:
        return render(request, 'examples/sendEmail.html', {'mail' : contact })


#Add Category
def addCategories(request):
    if request.method == 'POST':
        myform = addCategoryForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('loggedin')
        else:
            context = {
                'myform': myform
            }
            return render(request, 'examples/addCategories.html', context)
    else:
        myform = addCategoryForm()
        return render(request, 'examples/addCategories.html', {'myform': myform})


class ShowCategories(APIView):
    def get(self, instance):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ViewAllPosts_API(APIView):
    def get(self, instance):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class ProductByCategoryAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(category=self.kwargs['pk'])
        queryset = Product.objects.filter(pk=self.kwargs['pk'])
        return queryset


class ProductDetails(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        query_set = Product.objects.get(id=self.kwargs['pk'])
        return query_set


class ConfirmOrder(generics.GenericAPIView):

    def post(self, request):
        serializer = OrderItemsSerializer
        order_items = [
            {
                'user': request.user.id,
                'product': Product.objects.get(id=1),
                'product_quantity': 2,
                'product_cost_total': (Product.objects.get(id=1)).product_price * 2,
                'order_number': 1,
            },
            {
                'user': request.user.id,
                'product': Product.objects.get(id=1),
                'product_quantity': 1,
                'product_cost_total': (Product.objects.get(id=1)).product_price * 1,
                'order_number': 1,
            }
        ]
        last_obj = Order.objects.last()
        order_number = last_obj.order_number+1
        for item in order_items:
            order_item_obj = Orderitems.objects.create(
                user=item['user'],
                product=item['product'],
                product_quantity=item['product_quantity'],
                product_cost_total=item['product_cost_total'],
                order_number=order_number,
            )
        message = 'Order items saved successfully '
        return Response(message)


class CreateOrder(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def post(self, order_number):
        last_obj = Order.objects.last()
        order_number = last_obj.order_number+1
        Order.objects.create(
            user=self.request.user.id,
            order_number=order_number,
            total_products=Orderitems.objects.filter(order_number=order_number).count(),
            total_cost=240,
            shipping_address='shipping address',
            additional_requirements='additional_requirements',
            driver=Driver.objects.get(id=1),
            order_status='Initiated',
        )
        message = 'Order Created Successfully'
        driver_obj = Driver.objects.get(id=1)
        Notifications.objects.create(
            Driver=driver_obj,
            message='You have an order Delivery Request'
        )
        return Response(message)


class NewOrdersListAPI(APIView):

    def get(self):
        notifs = Notifications.objects.filter(status=False,Driver=Driver.objects.get(id=self.kwargs['pk']))
        return notifs


@api_view (['PUT'])
def notifMarkAsRead(request, pk):
    notif_obj = Notifications.objects.get(id=pk)
    data = {'status': True}
    if request.method == 'PUT':
        serializer = NotificationSerializer(notif_obj, data= data)
        if serializer.is_valid():
            message = " Notification Marked as Read Successfully"
            serializer.save()
            return Response(data=message)


@api_view (['PUT'])
def orderAccepted(request, pk):
    notif_obj = get_object_or_404(Notifications, id=pk)
    order_obj = notif_obj.Order
    order_obj.order_status="Accepted"
    order_obj.save()
    return Response("Order Accepted Successfully")


@api_view(['PUT'])
def cancelOrder(request, pk):
    notif_obj = get_object_or_404(Notifications, id=pk)
    order_obj = notif_obj.Order
    order_obj.order_status="Canceled By Driver"
    order_obj.save()
    return Response("Order Cancelled Successfully")


@api_view(['PUT'])
def deliverorder(request, pk):
    order_obj = get_object_or_404(Order, id=pk)
    order_obj.order_status="Delivered"
    order_obj.save()
    return Response("Order Delivered Successfully")


class ActiveOrdersListAPI(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order_objects = Order.objects.filter(driver=self.kwargs['pk'], order_status="Accepted")
        return order_objects


class CompletedOrdersListAPI(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order_objects = Order.objects.filter(driver=self.kwargs['pk'], order_status="Delivered", order_date=date.today())
        return order_objects


class CancelledOrdersListAPI(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order_objects = Order.objects.filter(driver=self.kwargs['pk'], order_status="Canceled By Driver", order_date=date.today())
        return order_objects
