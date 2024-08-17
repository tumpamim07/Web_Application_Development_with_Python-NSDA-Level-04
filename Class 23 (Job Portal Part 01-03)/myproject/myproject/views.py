from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

def SignInPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            return redirect("dashboardPage")
        else:
            return redirect("SignInPage")
        
    return render(request,'SignInPage.html')

def SignupPage(request):
    
    if request.method == 'POST':
        
        displayName=request.POST.get('displayname')
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        Confirmpassword=request.POST.get('confirm_password')
        userType=request.POST.get('user_type')
        Firstname=request.POST.get('firstname')
        Lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        db=request.POST.get('dob')
        Blood=request.POST.get('blood')
        Gender=request.POST.get('gender')
        address=request.POST.get('address')
        Image=request.FILES.get('image')
        
        if pass_word==Confirmpassword:
            
            user=Custom_user.objects.create_user(username=user_name,password=pass_word)
            user.display_name=displayName
            user.user_type=userType
            user.FirstName=Firstname
            user.LastName=Lastname
            user.DOB=db
            user.blood=Blood
            user.gender=Gender
            user.Image=Image
            user.email=email
            user.address=address
            
            user.save()
            
            return redirect('SignInPage')
        else:
            return redirect("SignupPage")
    return render(request,'SignupPage.html')

@login_required
def LogoutPage(request):
    logout(request)
    return redirect("SignInPage")

@login_required
def dashboardPage(request):
    return render(request,'dashboardPage.html')

@login_required
def addJobPage(request):
    if request.method=='POST':
        jobTitle=request.POST.get('jobTitle')
        companyName=request.POST.get('companyName')
        address=request.POST.get('address')
        companyDescription=request.POST.get('companyDescription')
        jobDescription=request.POST.get('jobDescription')
        qualification=request.POST.get('qualification')
        salaryInformation=request.POST.get('salaryInformation')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        
        job=JobModel(
           JobTitle=jobTitle,
           CompanyName=companyName,
           Address=address,
           CompanyDescription=companyDescription,
           JobDescription=jobDescription,
           Qualification=qualification,
           SalaryInformation=salaryInformation,
           Deadline=deadline,
           Designation=designation,
           Experience=experience,
        )
        job.save()
        return redirect("ViewallJob")
    return render(request,'addJobPage.html')

def ViewallJob(request):
    job=JobModel.objects.all()
    mydic={
        'job':job
    }
    return render(request,'ViewallJob.html',mydic)

def deleteviewalljob(request,myid):
    job=JobModel.objects.get(id=myid)
    job.delete()
    return redirect("ViewallJob")

def editjob(request,myid):
    job=JobModel.objects.get(id=myid)
    mydict={
        'jobs':job
    }
    return render(request,'editjob.html',mydict)


@login_required
def updatejob(request):
    if request.method=='POST':
        id=request.POST.get('id')
        jobTitle=request.POST.get('jobTitle')
        companyName=request.POST.get('companyName')
        address=request.POST.get('address')
        companyDescription=request.POST.get('companyDescription')
        jobDescription=request.POST.get('jobDescription')
        qualification=request.POST.get('qualification')
        salaryInformation=request.POST.get('salaryInformation')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        
        job=JobModel(
           id=id,
           JobTitle=jobTitle,
           CompanyName=companyName,
           Address=address,
           CompanyDescription=companyDescription,
           JobDescription=jobDescription,
           Qualification=qualification,
           SalaryInformation=salaryInformation,
           Deadline=deadline,
           Designation=designation,
           Experience=experience,
        )
        job.save()
    return redirect("ViewallJob")

def viewcard(request,myid):
    job=JobModel.objects.filter(id=myid)
    mydict={
        'job':job
    }
    return render(request,"viewcard.html",mydict)

@login_required
def profilePage(request):
    
    return render(request,'profilePage.html')

@login_required
def viewJobPage(request):
    
    return render(request,'viewJobPage.html')