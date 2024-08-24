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
    path('addjob/',addjob,name='addjob'),
    path('viewjob/',viewjob,name='viewjob'),
    path('deletejob/<str:myid>',deletejob,name='deletejob'),
    path('editjob/<str:myid>',editjob,name='editjob'),
    path('updatejob/',updatejob,name='updatejob'),
    path('viewsinglejob/<str:myid>',viewsinglejob,name='viewsinglejob'),
    path('profile',profile,name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)