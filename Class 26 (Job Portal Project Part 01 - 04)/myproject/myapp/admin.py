from django.contrib import admin
from myapp.models import *


class Custom_User_Display(admin.ModelAdmin):
    list_display=['username','bloodGroup','usertype']

admin.site.register(Custom_User_Model,Custom_User_Display)
admin.site.register(JobModel)
