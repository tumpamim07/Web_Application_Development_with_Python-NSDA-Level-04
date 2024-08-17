from django.contrib import admin
from myapp.models import *

class Custom_User_Display(admin.ModelAdmin):
    list_display=['display_name','username','gender','blood']

admin.site.register(Custom_user,Custom_User_Display)
admin.site.register(JobModel)

