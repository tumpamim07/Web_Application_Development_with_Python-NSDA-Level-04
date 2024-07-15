from django.shortcuts import render,redirect,HttpResponse
from myapp.models import *

def home(request):
    return render(request,'home.html')

def studentpage(request):
    student=StudentModel.objects.all()
    mydic={
        'std':student
    }
    return render(request,'studentpage.html',mydic)

def addstudentpage(request):

    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        cou=request.POST.get('country')

        stdn=StudentModel(
            FirstName=fname,
            LastName=lname,
            Department=dep,
            Country=cou,
        )

        stdn.save()
        return redirect("studentpage")
    return render(request,'addstudentpage.html')

def deletestudentpage(request,myid):
    stdnt=StudentModel.objects.get(id=myid)
    stdnt.delete()
    return redirect("studentpage")

def editstudentpage(request,myid):
    stdnt=StudentModel.objects.filter(id=myid)
    mydict={
        'std':stdnt
    }
    return render(request,'editstudentpage.html',mydict)

def updatestudentpage(request):
    if request.method=='POST':
        myid=request.POST.get('studentid')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        count=request.POST.get('country')

        stdn=StudentModel(
            id=myid,
            FirstName=fname,
            LastName=lname,
            Department=dep,
            Country=count,
        )
        stdn.save()
        return redirect("studentpage")
    

def viewstudent(request,myid):
    student=StudentModel.objects.filter(id=myid)
    mydict={
        'student':student
    }
    return render(request,'viewstudent.html',mydict)

