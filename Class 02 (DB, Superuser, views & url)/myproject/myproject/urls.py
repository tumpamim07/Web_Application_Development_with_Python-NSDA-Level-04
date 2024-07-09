from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Homepage',Homepage,name="Homepage"),
    path('Contact',Contact,name="Contact"),
    path('About',About,name="About"),
    path('Location',Location,name="Location"),
    path('Follow',Follow,name="Follow"),
]
