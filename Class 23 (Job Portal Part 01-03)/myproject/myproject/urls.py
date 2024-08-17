from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SignInPage,name='SignInPage'),
    path('SignupPage/', SignupPage,name='SignupPage'),
    path('dashboardPage/', dashboardPage,name='dashboardPage'),
    path('addJobPage/', addJobPage,name='addJobPage'),
    path('viewJobPage/', viewJobPage,name='viewJobPage'),
    path('ViewallJob/', ViewallJob,name='ViewallJob'),
    path('updatejob/', updatejob,name='updatejob'),
    path('deleteviewalljob/<str:myid>', deleteviewalljob,name='deleteviewalljob'),
    path('editjob/<str:myid>', editjob,name='editjob'),
    path('viewcard/<str:myid>', viewcard,name='viewcard'),
    
    
    path('profilePage/', profilePage,name='profilePage'),
    path('LogoutPage/', LogoutPage,name='LogoutPage'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
