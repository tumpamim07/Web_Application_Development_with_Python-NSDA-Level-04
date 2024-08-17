from django.contrib import admin

from myapp.models import *

class Custom_User_Display(admin.ModelAdmin):
    list_display=['display_name','user_name']
    
admin.site.register(Custom_User,Custom_User_Display)