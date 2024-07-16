from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='home'),
    path('candidate/', candidate,name='candidate'),
    path('addcandidate/', addcandidate,name='addcandidate'),
    path('deletepage/<str:myid>', deletepage,name='deletepage'),
    path('editpage/<str:myid>', editpage,name='editpage'),
    path('updatecandidate/', updatecandidate,name='updatecandidate'),
    path('viewpage/<str:myid>', viewpage,name='viewpage'),
]
