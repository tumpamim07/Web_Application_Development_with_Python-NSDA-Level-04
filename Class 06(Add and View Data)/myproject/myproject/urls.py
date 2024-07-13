from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('index/',index,name='index'),
    path('studentpage/',studentpage,name='studentpage'),
    path('teacherpage/',teacherpage,name='teacherpage'),
]
