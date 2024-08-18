from django.contrib import admin
from myapp.models import *
# Register your models here.
class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['fname','lname','blood_group','user_type']

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(JobModel)