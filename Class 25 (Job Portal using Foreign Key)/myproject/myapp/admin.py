from django.contrib import admin
from myapp.models import *

class Customer_user_display(admin.ModelAdmin):
    list_display=('username','display_name','email')
    
admin.site.register(Custome_User,Customer_user_display)
admin.site.register(job_portal)
