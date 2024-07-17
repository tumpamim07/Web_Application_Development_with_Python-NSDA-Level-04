from django.contrib import admin
from myapp.models import *

admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(DoctorModel)

# Register your models here.
