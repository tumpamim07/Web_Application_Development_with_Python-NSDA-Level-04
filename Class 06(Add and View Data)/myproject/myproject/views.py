from django.shortcuts import render,redirect,HttpResponse
from myApp.models import *

def Home(request):
    return HttpResponse("Hello")

def index(request):
    return render (request,'index.html')

def home(request):
    return render (request,'home.html')

def studentpage(request):

    student=StudentModel.objects.all()
    dict={
        
        'std':student 
    }
    return render (request,'studentpage.html',dict)

def teacherpage(request):
    teacher=TeacherModel.objects.all()
    mydict={
        'teach':teacher
    }
    return render (request,'teacherpage.html',mydict)