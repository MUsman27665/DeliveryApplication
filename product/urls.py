
import django.conf
from django.urls import path, include
from . import views
from .views import *
from django.conf.urls.static import static

from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    #Post
    path('createPost/', views.createPost, name='createPost'),
    path('displayPost/', views.displayPost, name='displayPost'),
    path('allPostsApi/', views.ViewAllPosts_API.as_view(), name='postsapi'),
    path("deletePost/<int:id>", views.deletePost, name='deletePost'),
    #Contact Us
    path('contactUs', contactUs.as_view(), name='contactUs'),
    path('displayQuery', views.displayQuery, name='displayQuery'),
    path('sendmail/<int:id>', views.sendmail, name='sendmail'),
    #Categories
    path('addCategories/', views.addCategories, name='addCategories'),
    path('displayCategories/', views.displayCategories, name='displayCategories'),
    path('showCategories/', views.ShowCategories.as_view(), name='showcategories'),
    #Products
    path('addProducts/', views.addProducts, name='addProducts'),
    path('productDetails/<int:pk>/', views.ProductDetails.as_view(), name='addProducts'),
    path('displayProducts/', views.displayProducts, name='displayProducts'),
    path('productsByCategoryAPI/<int:pk>/', views.ProductByCategoryAPI.as_view(), name=
         'productsByCategoryAPI'),

    # Add to Cart
    #path('addtocart/<int:pk>/', views.AddtoCartAPI.as_view(), name='addtocart'),
    path('confirmorder', views.ConfirmOrder.as_view(), name='confirmorder'),
    path('createorder', views.CreateOrder.as_view(), name='createorder'),
    path('listNewOrderAPI/<int:pk>/', views.NewOrdersListAPI.as_view(), name='listneworder'),#driver id
    path('NotifMarkAsRead/<int:pk>', views.notifMarkAsRead, name='notifmarkasread'),#notification id
    path('OrderAccepted/<int:pk>', views.orderAccepted, name='orderaccepted'), #notification id
    path('cancelorder/<int:pk>', views.cancelOrder, name='ordercancelled'), #notification id
    path('deliverorder/<int:pk>', views.deliverorder, name='DeliverOrder'), #order id
    path('CompletedOrdersListAPI/<int:pk>/',views.CompletedOrdersListAPI.as_view(), name='CompletedOrdersListAPI'), #driver id
    path('CancelledOrdersListAPI/<int:pk>/', views.CancelledOrdersListAPI.as_view(),
                       name='CompletedOrdersListAPI'),
    path('ActiveOrdersListAPI/<int:pk>/', views.ActiveOrdersListAPI.as_view(), name='activeorderslist')# driver id

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(django.conf.settings.MEDIA_URL, document_root=django.conf.settings.MEDIA_ROOT)

"""
    path('addDriver/', views.addDriver , name = 'addDriver'),
    path('showDrivers/', views.showDrivers , name = 'showDrivers'),
    path('updateDriver/<int:userid>', views.updateDriver , name = 'updateDriver'),
    path("deleteDriver/<int:id>", views.deleteDriver,name='deleteDriver'),



    Contact Us Api

    path('contactUs', contactUs.as_view(), name='contactUs'),
    # path('contactUs', views.contactUs, name='contactUs'),
    path('displayQuery', views.displayQuery, name='displayQuery'),
    path('sendmail/<int:id>', views.sendmail, name='sendmail'),

    #Category
    path('addCategories/', views.addCategories, name='addCategories'),
    path('showCategories/', views.ShowCategories.as_view(), name='showcategories'),
    #path('onecategoryproducts/<int:pk>/', views.onecategoryproducts(id=id))

    # Products
    path('productsByCategoryAPI/<int:pk>/', views.ProductByCategoryAPI.as_view(), name=
         'productsByCategoryAPI')
    """