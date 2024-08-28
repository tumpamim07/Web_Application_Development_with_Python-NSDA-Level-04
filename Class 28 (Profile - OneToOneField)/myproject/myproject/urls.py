from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SigninPage,name='SigninPage'),
    path('SignUpPage/', SignUpPage,name='SignUpPage'),
    path('dashboard/', dashboard,name='dashboard'),
    path('Logoutpage/', Logoutpage,name='Logoutpage'),
    path('profile/', profile,name='profile'),

    #chef 
    path('addrecipe/', addrecipe,name='addrecipe'),
    path('recipelist/', recipelist,name='recipelist'),
    path('viewpage/<str:id>', viewpage,name='viewpage'),

    #viewer

    path('viewrecipe/', viewrecipe,name='viewrecipe'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
