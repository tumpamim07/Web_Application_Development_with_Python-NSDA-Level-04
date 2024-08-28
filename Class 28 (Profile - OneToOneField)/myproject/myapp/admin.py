from django.contrib import admin
from myapp.models import *

class User_Display(admin.ModelAdmin):
    list_display=['username','email','usertype']

admin.site.register(UserModel,User_Display)
admin.site.register(RecipeModel)
admin.site.register(chefProfile)
admin.site.register(ViewerProfile)