from django.contrib import admin
from django.urls import path
from myproject.views import index,table

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',index,name="index"),
    path('table',table,name="table"),
]
