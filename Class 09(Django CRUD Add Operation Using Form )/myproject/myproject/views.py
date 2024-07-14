from django.shortcuts import render,redirect,HttpResponse
from myapp.models import *

def home(request):
    return render(request,'home.html')

def studentpage(request):
    student=studentModel.objects.all()

    mydic={
        'std':student
    }
    return render(request,'studentpage.html',mydic)

def addstudentpage(request):

    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        cit=request.POST.get('city')

        student=studentModel(
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=cit,
        )

        student.save()

        return redirect ("studentpage")
    return render(request,'addstudentpage.html')