from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SigninPage,name='SigninPage'),
    path('SignupPage/', SignupPage,name='SignupPage'),
]
