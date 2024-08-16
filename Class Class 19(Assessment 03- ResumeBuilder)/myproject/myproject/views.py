from django.shortcuts import render,redirect
from myapp.models import *

def home(request):
    return render(request,'home.html')

def resume(request):
    resume=resumeModel.objects.all()

    mydic={
        'resume':resume,
    }

    return render(request,'resume.html',mydic)


def addresume(request):

    if request.method=='POST':
        name=request.POST.get('firstname')
        add=request.POST.get('address')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        ima=request.FILES.get('propic')
        care=request.POST.get('career')
        certi=request.POST.get('certificate')
        proje=request.POST.get('project')
        refer=request.POST.get('reference')
        degr=request.POST.get('degree')
        instit=request.POST.get('institute')
        graduat=request.POST.get('graduation')
        compa=request.POST.get('company')
        posit=request.POST.get('position')
        sta=request.POST.get('start')
        en=request.POST.get('end')
        sof=request.POST.get('soft')
        har=request.POST.get('hard')

        resume=resumeModel(
            FullName=name,
            Address=add,
            EmailAddress=em,
            Profilepicture=ima,
            PhoneNumber=ph,
            CareerObjective=care,
            Certifications=certi,
            Projects=proje,
            References=refer,
            Degree=degr,
            Institution=instit,
            Graduationyear=graduat,
            Company=compa,
            Position=posit,
            StartDate=sta,
            EndDate=en,
            HardSkills=har,
            SoftSkills=sof,
        )
        resume.save()

        return redirect('resume')
    return render(request,'addresume.html')

def deletepage(request,myid):
    resume=resumeModel.objects.get(id=myid)
    resume.delete() 
    return redirect("resume")

def editpage(request,myid):
    resume=resumeModel.objects.filter(id=myid)
    mydict={
        'resume':resume,
    }
    return render(request,'editpage.html',mydict)


def updatepage(request):

    if request.method=='POST':
        sid=request.POST.get('id')
        name=request.POST.get('firstname')
        add=request.POST.get('address')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        ima=request.FILES.get('profilepicture')
        care=request.POST.get('career')
        certi=request.POST.get('certificate')
        proje=request.POST.get('project')
        refer=request.POST.get('reference')
        degr=request.POST.get('degree')
        instit=request.POST.get('institute')
        graduat=request.POST.get('graduation')
        compa=request.POST.get('company')
        posit=request.POST.get('position')
        sta=request.POST.get('start')
        en=request.POST.get('end')
        har=request.POST.get('hard')
        sof=request.POST.get('soft')

        if ima:
            resume=resumeModel(
                id=sid,
                FullName=name,
                Address=add,
                EmailAddress=em,
                Profilepicture=ima,
                PhoneNumber=ph,
                CareerObjective=care,
                Certifications=certi,
                Projects=proje,
                References=refer,
                Degree=degr,
                Institution=instit,
                Graduationyear=graduat,
                Company=compa,
                Position=posit,
                StartDate=sta,
                EndDate=en,
                SoftSkills=sof,
                HardSkills=har,
            )
            resume.save()
        else:
            resumeid=resumeModel.objects.get(id=sid)
            resume=resumeModel(
                id=sid,
                FullName=name,
                Address=add,
                EmailAddress=em,
                Profilepicture=resumeid.Profilepicture,
                PhoneNumber=ph,
                CareerObjective=care,
                Certifications=certi,
                Projects=proje,
                References=refer,
                Degree=degr,
                Institution=instit,
                Graduationyear=graduat,
                Company=compa,
                Position=posit,
                StartDate=sta,
                EndDate=en,
                SoftSkills=sof,
                HardSkills=har,
            )
            resume.save()
        
        return redirect('resume')
    
def viewpage(request,myid):
    resume=resumeModel.objects.get(id=myid)
    
    mydict={
        'resume':resume,
    }
    return render(request,'viewpage.html',mydict)