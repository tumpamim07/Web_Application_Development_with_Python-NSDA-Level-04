from django.shortcuts import render,redirect
from myapp.models import *

def home(request):
    resume=ResumeModel.objects.all()
    education=EducationModel.objects.all()
    work=WorkModel.objects.all()
    
    mydict={
        'resume':resume,
        'education':education,
        'work':work,
    }
    return render(request,'home.html',mydict)

def addresume(request):
    if request.method=="POST":
        ProfilePicture=request.FILES.get('ProfilePicture')
        FullName=request.POST.get('FullName')
        Address=request.POST.get('Address')
        PhoneNumber=request.POST.get('PhoneNumber')
        EmailAddress=request.POST.get('EmailAddress')
        CareerObjective=request.POST.get('CareerObjective')
        HardSkills=request.POST.get('HardSkills')
        SoftSkills=request.POST.get('SoftSkills')
        Certifications=request.POST.get('Certifications')
        Projects=request.POST.get('Projects')
        References=request.POST.get('References')
        Degree=request.POST.get('Degree')
        Institution=request.POST.get('Institution')
        GraduationYear=request.POST.get('GraduationYear')
        Company=request.POST.get('Company')
        Position=request.POST.get('Position')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        
        resume=ResumeModel(
            ProfilePicture=ProfilePicture,
            FullName=FullName,
            Address=Address,
            PhoneNumber=PhoneNumber,
            EmailAddress=EmailAddress,
            CareerObjective=CareerObjective,
            HardSkills=HardSkills,
            SoftSkills=SoftSkills,
            Certifications=Certifications,
            Projects=Projects,
            References=References,
        )
        education=EducationModel(
            Degree=Degree,
            Institution=Institution,
            GraduationYear=GraduationYear,
        )
        work=WorkModel(
            Company=Company,
            Position=Position,
            StartDate=StartDate,
            EndDate=EndDate,
            
        )
        resume.save()
        education.save()
        work.save()
        
        return redirect('home')
        
    return render(request,'addresume.html')

def deleteresume(request,myid):
    resume=ResumeModel.objects.get(id=myid)
    education=EducationModel.objects.get(id=myid)
    work=WorkModel.objects.get(id=myid)
    
    resume.delete()
    education.delete()
    work.delete()
    return redirect('home')

def editresume(request,myid):
    resume=ResumeModel.objects.get(id=myid)
    education=EducationModel.objects.get(id=myid)
    work=WorkModel.objects.get(id=myid)
    
    mydict={
        'resume':resume,
        'education':education,
        'work':work,
    }
    return render(request,'editresume.html',mydict)

def updateresume(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        ProfilePicture=request.FILES.get('ProfilePicture')
        FullName=request.POST.get('FullName')
        Address=request.POST.get('Address')
        PhoneNumber=request.POST.get('PhoneNumber')
        EmailAddress=request.POST.get('EmailAddress')
        CareerObjective=request.POST.get('CareerObjective')
        HardSkills=request.POST.get('HardSkills')
        SoftSkills=request.POST.get('SoftSkills')
        Certifications=request.POST.get('Certifications')
        Projects=request.POST.get('Projects')
        References=request.POST.get('References')
        Degree=request.POST.get('Degree')
        Institution=request.POST.get('Institution')
        GraduationYear=request.POST.get('GraduationYear')
        Company=request.POST.get('Company')
        Position=request.POST.get('Position')
        StartDate=request.POST.get('StartDate')
        EndDate=request.POST.get('EndDate')
        
        if ProfilePicture:
            resume=ResumeModel(
                id=myid,
                ProfilePicture=ProfilePicture,
                FullName=FullName,
                Address=Address,
                PhoneNumber=PhoneNumber,
                EmailAddress=EmailAddress,
                CareerObjective=CareerObjective,
                HardSkills=HardSkills,
                SoftSkills=SoftSkills,
                Certifications=Certifications,
                Projects=Projects,
                References=References,
                )
            education=EducationModel(
                id=myid,
                Degree=Degree,
                Institution=Institution,
                GraduationYear=GraduationYear,
                )
            work=WorkModel(
                id=myid,
                Company=Company,
                Position=Position,
                StartDate=StartDate,
                EndDate=EndDate,
                
                )
        else:
            resumeid=ResumeModel.objects.get(id=myid)
            resume=ResumeModel(
                id=myid,
                ProfilePicture=resumeid.ProfilePicture,
                FullName=FullName,
                Address=Address,
                PhoneNumber=PhoneNumber,
                EmailAddress=EmailAddress,
                CareerObjective=CareerObjective,
                HardSkills=HardSkills,
                SoftSkills=SoftSkills,
                Certifications=Certifications,
                Projects=Projects,
                References=References,
                )
            education=EducationModel(
                id=myid,
                Degree=Degree,
                Institution=Institution,
                GraduationYear=GraduationYear,
                )
            work=WorkModel(
                id=myid,
                Company=Company,
                Position=Position,
                StartDate=StartDate,
                EndDate=EndDate,
                
                )
        resume.save()
        education.save()
        work.save()
    return redirect('home')

def viewresume(request,myid):
    resume=ResumeModel.objects.get(id=myid)
    education=EducationModel.objects.get(id=myid)
    work=WorkModel.objects.get(id=myid)
    
    mydict={
        'resume':resume,
        'education':education,
        'work':work,
    }
    return render(request,'viewresume.html',mydict)