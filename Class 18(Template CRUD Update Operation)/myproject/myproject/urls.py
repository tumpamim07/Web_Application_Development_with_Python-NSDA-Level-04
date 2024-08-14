from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('editabout/<str:myid>', editabout, name='editabout'),
    path('updateabout/', updateabout, name='updateabout'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
