from django.contrib import admin
from myapp.models import *

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','usertype','gender']

admin.site.register(CustomUserModel,CustomUserModelDisplay)
admin.site.register(RecipeModel)
