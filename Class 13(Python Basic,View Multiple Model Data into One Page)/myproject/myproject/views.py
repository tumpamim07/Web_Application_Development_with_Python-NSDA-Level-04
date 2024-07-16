from django.shortcuts import render,redirect,HttpResponse
from myapp.models import *

def home(request):
    student=StudentModel.objects.all()
    teacher=TeacherModel.objects.all()
    doctor=DoctorModel.objects.all()
    mydic={
        'student':student,
        'teacher':teacher,
        'doctor':doctor,
    }
    return render(request,'home.html',mydic)
def studentpage(request):
    student=StudentModel.objects.all()
    mydic={
       'student':student 
    }
    return render(request,'studentpage.html',mydic)

def addstudentpage(request):
    if request.method=='POST':
        fname=request.POST.get('name')
        dep=request.POST.get('department')
        ci=request.POST.get('city')
        image=request.FILES.get('studentimage')

        student=StudentModel(
            StudentName=fname,
            Department=dep,
            City=ci,
            StudentImage=image,
        )
        student.save()
        return redirect('studentpage')
    return render(request,'addstudentpage.html')

def studentdelete(request,myid):
    students=StudentModel.objects.get(id=myid)
    students.delete()
    return redirect("studentpage")

def studentedit(request,myid):
    std=StudentModel.objects.filter(id=myid)
    mydic={
       'std':std 
    }
    return render(request,'studentedit.html',mydic)

def updatestudent(request):
    if request.method=='POST':
        sid=request.POST.get('stid')
        fname=request.POST.get('name')
        dep=request.POST.get('department')
        ci=request.POST.get('city')
        image=request.FILES.get('studentimage')

        student=StudentModel(
            id=sid,
            StudentName=fname,
            Department=dep,
            City=ci,
            StudentImage=image,
        )
        student.save()
        return redirect('studentpage')
    
def studentview(request,myid):
    views=StudentModel.objects.filter(id=myid)
    dic1={
        'views':views
    }
    return render(request,'studentview.html',dic1)

def teacherpage(request):
    teacher=TeacherModel.objects.all()
    mydic={
       'teacher':teacher 
    }
    return render(request,'teacherpage.html',mydic)

def addteacherpage(request):
    if request.method=='POST':
        fname=request.POST.get('name')
        dep=request.POST.get('department')
        ci=request.POST.get('city')
        im=request.FILES.get('teacherimage')

        teacher=TeacherModel(
            TeacherName=fname,
            TDepartment=dep,
            TCity=ci,
            TImage=im,
        )
        teacher.save()
        return redirect('teacherpage')
    return render(request,'addteacherpage.html')

def teacherdelete(request,myid):
    teachers=TeacherModel.objects.get(id=myid)
    teachers.delete()
    return redirect("teacherpage")

def teacheredit(request,myid):
    tct=TeacherModel.objects.filter(id=myid)
    mydic={
       'tct':tct 
    }
    return render(request,'teacheredit.html',mydic)

def updateteacher(request):
    if request.method=='POST':
        sid=request.POST.get('stid')
        fname=request.POST.get('name')
        dep=request.POST.get('department')
        ci=request.POST.get('city')
        im=request.FILES.get('teacherimage')

        teacher=TeacherModel(
            id=sid,
            TeacherName=fname,
            TDepartment=dep,
            TCity=ci,
            TImage=im,
        )
        teacher.save()
        return redirect('teacherpage')
    
def teacherview(request,myid):
    views=TeacherModel.objects.filter(id=myid)
    dic1={
        'views':views
    }
    return render(request,'teacherview.html',dic1)

def doctorpage(request):
    doctor=DoctorModel.objects.all()
    mydic={
       'doctor':doctor 
    }
    return render(request,'doctorpage.html',mydic)


def adddoctorpage(request):
    if request.method=='POST':
        fname=request.POST.get('name')
        dep=request.POST.get('department')
        ci=request.POST.get('city')
        image=request.FILES.get('doctorimage')

        doctor=DoctorModel(
            DoctorName=fname,
            DDepartment=dep,
            DCity=ci,
            DImage=image,
        )
        doctor.save()
        return redirect('doctorpage')
    return render(request,'adddoctorpage.html')

def doctordelete(request,myid):
    doctors=DoctorModel.objects.get(id=myid)
    doctors.delete()
    return redirect("doctorpage")
   
def doctoredit(request,myid):
    dct=DoctorModel.objects.filter(id=myid)
    mydic={
       'dct':dct 
    }
    return render(request,'doctoredit.html',mydic)

def updatedoctor(request):
    if request.method=='POST':
        sid=request.POST.get('stid')
        fname=request.POST.get('name')
        dep=request.POST.get('department')
        ci=request.POST.get('city')
        image=request.FILES.get('doctorimage')

        doctor=DoctorModel(
            id=sid,
            DoctorName=fname,
            DDepartment=dep,
            DCity=ci,
            DImage=image,
        )
        doctor.save()
        return redirect('doctorpage')
    
def doctorview(request,myid):
    views=DoctorModel.objects.filter(id=myid)
    dic1={
        'views':views
    }
    return render(request,'doctorview.html',dic1)
