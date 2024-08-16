from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home,name='home'),
    path('resume/', resume,name='resume'),
    path('addresume/', addresume,name='addresume'),
    path('deletepage/<str:myid>', deletepage,name='deletepage'),
    path('editpage/<str:myid>', editpage,name='editpage'),
    path('viewpage/<str:myid>', viewpage,name='viewpage'),
    path('updatepage/', updatepage,name='updatepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
