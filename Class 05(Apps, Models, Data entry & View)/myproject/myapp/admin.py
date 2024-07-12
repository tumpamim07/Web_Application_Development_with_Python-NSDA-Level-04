from django.contrib import admin

from myapp.models import *

admin.site.register(studentModel)
admin.site.register(teacherModel)
admin.site.register(workerModel)
admin.site.register(subjectModel)
admin.site.register(classModel)
