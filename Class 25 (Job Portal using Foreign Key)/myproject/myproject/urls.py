from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SignUppage/', SignUppage,name='SignUppage'),
    path('', SignInpage,name='SignInpage'),
    path('dashboardPage/', dashboardPage,name='dashboardPage'),
    path('LogoutPage/', LogoutPage,name='LogoutPage'),
    path('profile/', profile,name='profile'),
    
    #recruiter 
    path('addjob/', addjob,name='addjob'),
    path('joblist/', joblist,name='joblist'),
    path('deletepage/<str:id>', deletepage,name='deletepage'),
    path('viewpage/<str:id>', viewpage,name='viewpage'),
    path('editpage/<str:id>', editpage,name='editpage'),
    path('updatepage/', updatepage,name='updatepage'),
    
    #seeker
    path('viewjob/', viewjob,name='viewjob'),
]
