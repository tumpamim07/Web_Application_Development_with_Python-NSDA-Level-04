from django.shortcuts import render,redirect,HttpResponse
from myapp.models import *

def home(request):
    return render(request,'home.html')

def studentpage(request):
    student=StudentModel.objects.all()
    dict={
        'student':student
    }
    return render(request,'studentpage.html',dict)

def addstudentpage(request):
    if request.method=='POST':
        name=request.POST.get('firstname')
        roll=request.POST.get('roll')
        de=request.POST.get('department')
        imag=request.FILES.get('image')

        studen=StudentModel(
            Name=name,
            Roll=roll,
            Department=de,
            Image=imag,
        )
        studen.save()
        return redirect('studentpage')
    return render(request,'addstudentpage.html')

def studentdelete(request,myid):
    studnt=StudentModel.objects.get(id=myid)
    studnt.delete()
    return redirect('studentpage')

def studentedit(request,myid):
    std=StudentModel.objects.filter(id=myid)
    dictt={
        'std':std
    }
    return render(request,'studentedit.html',dictt)

def studentupdate(request):
    if request.method=='POST':
        id=request.POST.get('studentid')
        name=request.POST.get('firstname')
        roll=request.POST.get('roll')
        de=request.POST.get('department')
        imag=request.FILES.get('image')

        studen=StudentModel(
            id=id,
            Name=name,
            Roll=roll,
            Department=de,
        )
        if imag:
            studen.Image=imag
            studen.save()
            
        studen.save()
    return redirect('studentpage')

def studentview(request,myid):
    student=StudentModel.objects.filter(id=myid)

    mydic={
        'student':student
    }
    return render(request,'studentview.html',mydic)

