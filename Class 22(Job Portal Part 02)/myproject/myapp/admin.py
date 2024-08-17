from django.contrib import admin
from myapp.models import *

class Customer_User_Display(admin.ModelAdmin):
    list_display=['display_name','email','Blood','Gender']

admin.site.register(Customet_User,Customer_User_Display)
