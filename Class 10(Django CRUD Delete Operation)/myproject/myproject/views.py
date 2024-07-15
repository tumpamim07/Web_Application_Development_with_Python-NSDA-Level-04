from django.shortcuts import render,redirect,HttpResponse
from myApp.models import StudentModel

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
        cit=request.POST.get('city')

        student=StudentModel(
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=cit,
        )  
        student.save()
        return redirect("studentpage")
    return render(request,'addstudentpage.html')

def deletestudentpage(request,myid):
    stdnT=StudentModel.objects.get(id=myid)
    stdnT.delete()
    return redirect("studentpage")