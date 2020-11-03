from itertools import count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from notify.signals import notify

from .models import Product
from .serializers import ProductSerializer, OrderSerializer, OrderItemsSerializer, NotificationSerializer
from .models import *
from .forms import *
from .forms import createPostForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from .serializers import ContactUsSerializer, CategorySerializer, PostSerializer
from rest_framework import generics, permissions

from django.core.mail import send_mail
from .models import Notifications
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMessage



# from django.utils import simplejson as abc
# Create your views here.

"""
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
                context= {'LoginError': 'Please enter credentials'}
                raise forms.ValidationError("The two password fields must match.")
            else:
                Driver.objects.create(
                    firstname = request.POST['first_name'],
                    lastname  = request.POST['last_name'],
                    email     = request.POST['email'],
                    contact   = request.POST['number'],
                    address   = request.POST['address'],
                    password  = request.POST['password'],
                    image     = request.FILES['image']
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

    print("",settings.MEDIA_ROOT)

    image_source = settings.SERVER_URL+'/media/'
    
    context={
        'drivers'      : all_drivers ,
        'image_source' : image_source
    }

    return render(request, 'examples/showDriver.html',context)
    
@csrf_exempt
def updateDriver(request,userid):
    if request.method == 'POST':
        print('helooooooooooooooooooooooooooooo')
        drive = Driver.objects.get(id=userid)
        print(drive)
        
        if (request.POST['firstname'] is not None and request.POST['lastname'] is not None):
            
            print("Pic is coming.......")
            drive.firstname = request.POST['firstname']
            drive.lastname  = request.POST['lastname']
            drive.address   = request.POST['address']
            print('99999999999999999999999999999999')
            print('99999999999999999999999999999999')
            
            # if (request.POST['image'] is None):
            # profile_pics    = request.FILES['image']
            # drive.image = profile_pics

            image_path      = 'media/contacts/'
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
            return render(request,'examples/updateDriver.html',{'obj':user_id})            
    else:
        obj = Driver.objects.get(id=userid)
        return render(request,'examples/updateDriver.html',{'obj':obj})


@csrf_exempt
def deleteDriver(request,id):

    # if request.method=='POST':
    #     obj=StudentForm(request.POST,request.FILES)

    #     Student.objects.get(id=id).delete()
    #     return redirect('/')
    # else:
    print('wowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
    drive = Driver.objects.get(id=id).delete()
    return redirect('../showDrivers/')
"""


@csrf_exempt
# @login_required
def createPost(request):
    
    # if request.method == 'POST':
    #     print(request.user)
    #     # print(request.FILES['image'])
    #     print(request.POST['last_name'])
    #     print(request.POST['password'])
    #     print(request.POST['confirm_password'])
    #     image_source ='contacts/images/'+request.POST['image']

    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    #     if password and confirm_password:
    #         if password != confirm_password:
    #             context= {'LoginError': 'Please enter credentials'}
    #             raise forms.ValidationError("The two password fields must match.")
    #         else:
    #             Driver.objects.create(
    #                 firstname = request.POST['first_name'],
    #                 lastname  = request.POST['last_name'],
    #                 email     = request.POST['email'],
    #                 contact   = request.POST['number'],
    #                 address   = request.POST['address'],
    #                 password  = request.POST['password'],
    #                 image     = image_source
    #             )
        
        
        
    #     return redirect('loggedin')

    # else:

    #     return render(request, 'examples/createPost.html')

    if request.method=='POST':
        myform = createPostForm(request.POST,request.FILES)

        if myform.is_valid():
            
            
            myform.save()
            return redirect('../loggedin/')
        else:
            print(myform.errors)
            context = {
                'myform':myform
            }
            return render(request, 'examples/createPost.html', context)
    else:
        myform = createPostForm()
        print(myform.errors)
        return render(request,'examples/createPost.html',{'myform':myform})


def displayCategories(request):
    all_category = Category.objects.all()
    print(all_category)

    print("", settings.MEDIA_ROOT)

    image_source = settings.SERVER_URL + '/media/'
    print(image_source)
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
            print(myform.errors)
            context = {
                'myform': myform
            }
            return render(request, 'examples/addProducts.html', context)
    else:
        myform = addProductForm()
        print(myform)
        return render(request, 'examples/addProducts.html', {'myform': myform})


def displayProducts(request):
    all_products = Product.objects.all()
    print(all_products)

    print("", settings.MEDIA_ROOT)

    image_source = settings.SERVER_URL + '/media/'
    print(image_source)
    context = {
        'products': all_products,
        'image_source': image_source
    }

    return render(request, 'examples/displayProducts.html', context)



def displayPost(request):
    
    all_posts = Post.objects.all()
    print(all_posts)

    print("",settings.MEDIA_ROOT)

    image_source = settings.SERVER_URL+'/media/'
    print(image_source)
    context={
        'posts'      : all_posts ,
        'image_source' : image_source
    }

    return render(request, 'examples/displayPost.html',context)


def deletePost(request,id):

    # if request.method=='POST':
    #     obj=StudentForm(request.POST,request.FILES)

    #     Student.objects.get(id=id).delete()
    #     return redirect('/')
    # else:
    print('nowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
    drive = Post.objects.get(id=id).delete()
    return redirect('../displayPost/')


#Contact Us Api


# @api_view(["POST"])
# @permission_classes((AllowAny,))
# # @csrf_exempt
# @generics.GenericAPIView
# def contactUs(request,self,format=None):
#     serializer_class = ContactUsSerializer
#     if request.method == "POST":
#         serializer = self.get_serializer(data=request.data)

#         print(request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         print(user)
#         # return Response(status=status.HTTP_201_CREATED)        
#         # send_mail('Subject here', 'Here is the message', 'asimraza336@gmail.com', ['asimraza336@gmail.com'],fail_silently=False)

#         return Response(
#             {
#                 'Msg': 'Product successfully added'
#             },
#             status=HTTP_200_OK)

class contactUs(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContactUsSerializer
    print('outttttttttttttttttttttttttttttttttttttttttt')

    def post(self, request, *args, **kwargs):
        print('innnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        # return Response(status=status.HTTP_201_CREATED)        
        # send_mail('Subject here', 'Here is the message', 'asimraza336@gmail.com', ['asimraza336@gmail.com'],fail_silently=False)

        return Response(
            {
                'Msg': 'Product successfully added'
            },
            status=HTTP_200_OK)


def displayQuery(request):
    
    all_queries = ContactUs.objects.all()
    print(all_queries)

    # print("",settings.MEDIA_ROOT)

    # image_source = settings.SERVER_URL+'/media/'
    # print(image_source)
    context={
        'all_queries'      : all_queries 
        # 'image_source' : image_source
    }

    return render(request, 'examples/displayQuery.html',context)


# def sendemail(request):
    
#     all_queries = ContactUs.objects.all()
#     print(all_queries)

#     send_mail('Subject here', 'Here is the message', 'hk43341@gmail.com', ['asimraza336@gmail.com'],fail_silently=False)
#     context={
#         'all_queries'      : all_queries 
#         # 'image_source' : image_source
#     }

#     return render(request, 'examples/displayQuery.html',context)

# class sendmail(generics.GenericAPIView):
#     print('outttttttttttttttttttttttttttttttttttttttttt')
#     def post(self, request, *args, **kwargs):

#         print(request.data)
#         subject = request.data.get('subject')
#         body    =request.data.get('body')
#         email   = request.data.get('email')
#         msg=send_mail(subject,body,settings.EMAIL_HOST_USER,[email],fail_silently=False)
#         return Response(
#             {
#                 'res': msg
#             },
#             status=HTTP_200_OK)

# @csrf_exempt
def sendmail(request,id):
    print(request.data)
    subject = request.data.get('subject')
    body    =request.data.get('body')
    email   = request.data.get('email')
    contact = ContactUs.objects.get(id=id)
    if request.method=='POST':
        print('asimmmmmmmmmmmmmmmmmmmmmmmmm')
        print(request.POST)
        subject = request.POST['subject']
        body    = request.POST['body']
        email   = contact.email
        print(email)
        msg=send_mail(subject,body,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        print(msg)
        return redirect('../displayQuery')
    else:
        print('wow')
    return render(request, 'examples/sendEmail.html',{'mail' : contact })




#Add Category

def addCategories(request):
    print('-----------------------------------------')

    # print(self.request.user)
    if request.method == 'POST':
        myform = addCategoryForm(request.POST, request.FILES)
        print(request.POST)
        if myform.is_valid():
            print(myform)
            myform.save()
            return redirect('loggedin')
        else:
            print(myform.errors)
            context = {
                'myform': myform
            }
            return render(request, 'examples/addCategories.html', context)
    else:
        myform = addCategoryForm()
        return render(request, 'examples/addCategories.html', {'myform': myform})

    # Product.objects.create(email="vale@vale.io", user=product_id)
    
    
    # return Response(status=status.HTTP_201_CREATED)        


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
        """queryset = Product.objects.filter(pk=self.kwargs['pk'])"""
        return queryset


class ProductDetails(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    """query_set = Product.objects.get(id=)"""

    def get_object(self):
        query_set = Product.objects.get(id=self.kwargs['pk'])
        return query_set


class ConfirmOrder(generics.GenericAPIView):

    def post(self, request):
        serializer = OrderItemsSerializer
        order_items = [
            {
                'user': request.user.id,
                #'order': 1,
                'product': Product.objects.get(id=1),
                'product_quantity': 2,
                'product_cost_total': (Product.objects.get(id=1)).product_price * 2,
                'order_number': 1,
            },
            {
                'user': request.user.id,
                #'order': Order.objects.get,
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
                #order=item['order'],
                product=item['product'],
                product_quantity=item['product_quantity'],
                product_cost_total=item['product_cost_total'],
                order_number=order_number,
            )
            #order_item_obj.save()
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
            total_cost=240,#Orderitems.objects.filter(order_number=1).aggregate(sum('product_cost_total')),
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
        # serializer = OrderSerializer
        notifs = Notifications.objects.filter(status=False,Driver=Driver.objects.get(id=self.kwargs['pk']))
        # serializer = NotificationSerializer(posts, many=True)
        return notifs

"""
class NotifMarksAsRead(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        Notifications.objects.filter(id=self.kwargs['pk']).update(status=True)
"""
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
    """
        def get(self, instance):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    notif_obj = get_object_or_404(Notifications, id=pk)
    order_obj = notif_obj.Order
    order_obj.order_status="Accepted"
    order_obj.save()
    return Response("Order Accepted Successfully")
    """


"""print("notification marked as read")

    def get_queryset(self):
        Notifications.objects.filter(id=self.kwargs['pk']).update(status=True)
        
"""




"""
class AddtoCartAPI(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    #serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        cart_item, created = Cart.objects.get_or_create(
            product=product,
            user=request.user,
            order_confirmation_status=False
        )
        Cart_qs = Cart.objects.filter(user=request.user, order_confirmation_status=False)
        if Cart_qs.exists():
            cart = Cart_qs[0]
            if cart.products.filter(product__id=self.kwargs['pk']).exists():
                cart_item.quantity += 1
                cart_item.save()
                #messages.info(request, "This item quantity was updated.")
                return redirect("core:order-summary")
            else:
                order.items.add(order_item)
                messages.info(request, "This item was added to your cart.")
                return redirect("core:order-summary")
        users_cart = get_object_or_404(Cart, user=self.request.user.id, order_confirmation_status=False)
        #cart_item = get_object_or_404(Cart, user=self.request.user)
        if users_cart.exists():
            Cart.objects.create(
                cart_number=self.request.user.id,
                product=product,
                product_quantity=1,

            )
            users_cart.save()



        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        return Response(
            {
                'Msg': 'Product successfully added to Cart'
            },
            status=HTTP_200_OK)
    """

"""def onecategoryproducts(APIView):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category, many=False)
    category_products = Product.objects.filter(product_id=id)
    return (serializer.data)"""

