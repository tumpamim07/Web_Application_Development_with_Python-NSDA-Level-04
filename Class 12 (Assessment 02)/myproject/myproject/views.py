from django.shortcuts import render,redirect,HttpResponse
from myapp.models import *

def home(request):
    return render(request,'home.html')

def candidate(request):
    candidate=CandidateModel.objects.all()
    mydic={
        'can':candidate
    }
    return render(request,'candidate.html',mydic)

def addcandidate(request):
    if request.method=='POST':
        fname=request.POST.get('fullname')
        em=request.POST.get('email')
        ph=request.POST.get('phonenumber')
        add=request.POST.get('address')
        job=request.POST.get('jobtitle')
        lin=request.POST.get('linkedinprofile')
        uni=request.POST.get('university')
        deg=request.POST.get('degree')
        lan=request.POST.get('languages')
        ye=request.POST.get('yearsofexperience')
        
        candid=CandidateModel(
            full_name=fname,
            email=em,
            phone_number=ph,
            address=add,
            job_title=job,
            linkedin_profile=lin,
            university=uni,
            degree=deg,
            languages=lan,
            years_of_experience=ye,
        )
        
        candid.save()
        return redirect("candidate")
    return render(request,'addcandidate.html')

def deletepage(request,myid):
    candi=CandidateModel.objects.get(id=myid)
    candi.delete()
    return redirect("candidate")

def editpage(request,myid):
    candidate=CandidateModel.objects.filter(id=myid)
    dic1={
        'cand':candidate
    }
    return render(request,'editpage.html',dic1)

def updatecandidate(request):
     if request.method=='POST':
        id=request.POST.get('studentid')
        fname=request.POST.get('fullname') 
        em=request.POST.get('email')
        ph=request.POST.get('phonenumber')
        add=request.POST.get('address')
        job=request.POST.get('jobtitle')
        lin=request.POST.get('linkedinprofile')
        uni=request.POST.get('university')
        deg=request.POST.get('degree')
        lan=request.POST.get('languages')
        ye=request.POST.get('yearsofexperience')
        
        candid=CandidateModel(
            id=id,
            full_name=fname,
            email=em,
            phone_number=ph,
            address=add,
            job_title=job,
            linkedin_profile=lin,
            university=uni,
            degree=deg,
            languages=lan,
            years_of_experience=ye,
        )
        
        candid.save()
        return redirect("candidate")
    
def viewpage(request,myid):
    viewc=CandidateModel.objects.filter(id=myid)
    dic1={
        'viewc':viewc
    }
    return render(request,'viewpage.html',dic1)