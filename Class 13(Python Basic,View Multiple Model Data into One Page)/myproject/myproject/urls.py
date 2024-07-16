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
    path('updatestudent/', updatestudent,name='updatestudent'),
    path('studentview/<str:myid>', studentview,name='studentview'),

    path('teacherpage/', teacherpage,name='teacherpage'),
    path('addteacherpage/', addteacherpage,name='addteacherpage'),
    path('teacherdelete/<str:myid>', teacherdelete,name='teacherdelete'),
    path('teacheredit/<str:myid>', teacheredit,name='teacheredit'),
    path('updateteacher/', updateteacher,name='updateteacher'),
    path('teacherview/<str:myid>', teacherview,name='teacherview'),

    path('doctorpage/', doctorpage,name='doctorpage'),
    path('adddoctorpage/', adddoctorpage,name='adddoctorpage'),
    path('doctordelete/<str:myid>', doctordelete,name='doctordelete'),
    path('doctoredit/<str:myid>', doctoredit,name='doctoredit'),
    path('updatedoctor/', updatedoctor,name='updatedoctor'),
    path('doctorview/<str:myid>', doctorview,name='doctorview'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
