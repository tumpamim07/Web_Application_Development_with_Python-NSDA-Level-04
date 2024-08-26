from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('profile/',profile,name='profile'),
    path('addrecipe/',addrecipe,name='addrecipe'),
    path('viewallrecipe/',viewallrecipe,name='viewallrecipe'),
    path('singlerecipeview/<str:myid>',singlerecipeview,name='singlerecipeview'),
    path('deleterecipe/<str:myid>',deleterecipe,name='deleterecipe'),
    path('editrecipe/<str:myid>',editrecipe,name='editrecipe'),
    path('udpaterecipe/',udpaterecipe,name='udpaterecipe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)