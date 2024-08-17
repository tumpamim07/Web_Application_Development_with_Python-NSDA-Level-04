from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SignupPage/', SignupPage, name='SignupPage'),
    path('', SigninPage, name='SigninPage'),
]
