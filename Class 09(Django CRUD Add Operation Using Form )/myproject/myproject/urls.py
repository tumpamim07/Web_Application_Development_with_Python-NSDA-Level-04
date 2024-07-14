from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='home'),
    path('studentpage/', studentpage,name='studentpage'),
     path('addstudentpage/', addstudentpage,name='addstudentpage'),
]
