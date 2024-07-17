from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='home'),
    path('studentpage/', studentpage,name='studentpage'),
    path('addstudentpage/', addstudentpage,name='addstudentpage'),
    path('studentdelete/<str:myid>', studentdelete,name='studentdelete'),
    path('studentedit/<str:myid>', studentedit,name='studentedit'),
    path('studentupdate/', studentupdate,name='studentupdate'),
    path('studentview/<str:myid>', studentview,name='studentview'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
