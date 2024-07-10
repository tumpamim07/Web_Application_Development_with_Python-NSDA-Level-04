from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Base',Base,name="Base"),
    path('Home',Home,name="Home"),
    path('News',News,name="News"),
    path('Contact',Contact,name="Contact"),
    path('About',About,name="About"),
    path('Location',Location,name="Location"),
]
