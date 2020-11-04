
import django.conf
from django.urls import path, include
from . import views
from .views import *
from knox import views as knox_views
from django.conf.urls.static import static

from django.conf import settings
from django.contrib.auth import views as auth_views
# app_name = 'users'


urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('signup', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('login_api/', views.login_api , name='login_api'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(django.conf.settings.MEDIA_URL, document_root=django.conf.settings.MEDIA_ROOT)
