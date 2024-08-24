from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        profilePicture=request.FILES.get('profilePicture')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        bloodGroup=request.POST.get('bloodGroup')
        usertype=request.POST.get('usertype')
        
        if password==confirmpassword:
            
            user = Custom_User_Model.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                email=email,
                password=password,
                profilePicture=profilePicture,
                dob=dob,
                address=address,
                bloodGroup=bloodGroup,
                usertype=usertype,
            )
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
        
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')
    return render(request,'signin.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def dashboard(request):
    current_user=request.user
    if current_user.usertype == 'recruiter':
        jobs=JobModel.objects.filter(Created_by=request.user)
    else:
        jobs=JobModel.objects.all()
    jobDict={
        'jobs':jobs
    }
    return render(request,'dashboard.html',jobDict)

@login_required
def addjob(request):
    if request.method=="POST":
        JobTitle=request.POST.get('JobTitle')
        CompanyName=request.POST.get('CompanyName')
        Address=request.POST.get('Address')
        CompanyDescription=request.POST.get('CompanyDescription')
        JobDescription=request.POST.get('JobDescription')
        Qualification=request.POST.get('Qualification')
        SalaryInformation=request.POST.get('SalaryInformation')
        Deadline=request.POST.get('Deadline')
        Designation=request.POST.get('Designation')
        Experience=request.POST.get('Experience')
        
        job=JobModel(
            JobTitle=JobTitle,
            CompanyName=CompanyName,
            Address=Address,
            CompanyDescription=CompanyDescription,
            JobDescription=JobDescription,
            Qualification=Qualification,
            SalaryInformation=SalaryInformation,
            Deadline=Deadline,
            Designation=Designation,
            Experience=Experience,
            Created_by=request.user
        )
        job.save()
        return redirect('dashboard')
    return render(request,'recruiter/addjob.html')

@login_required
def viewjob(request):
    current_user=request.user
    if current_user.usertype == 'recruiter':
        jobs=JobModel.objects.filter(Created_by=request.user)
    else:
        jobs=JobModel.objects.all()
    mydict={
        'jobs':jobs
    }
    return render(request,'viewjob.html',mydict)

@login_required
def deletejob(request,myid):
    job=JobModel.objects.get(id=myid)
    job.delete()
    return redirect('dashboard')

@login_required
def editjob(request,myid):
    job=JobModel.objects.get(id=myid)
    mydict={
        'job':job
    }
    return render(request,'recruiter/editjob.html',mydict)

@login_required
def updatejob(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        JobTitle=request.POST.get('JobTitle')
        CompanyName=request.POST.get('CompanyName')
        Address=request.POST.get('Address')
        CompanyDescription=request.POST.get('CompanyDescription')
        JobDescription=request.POST.get('JobDescription')
        Qualification=request.POST.get('Qualification')
        SalaryInformation=request.POST.get('SalaryInformation')
        Deadline=request.POST.get('Deadline')
        Designation=request.POST.get('Designation')
        Experience=request.POST.get('Experience')
        
        if Deadline:
            job=JobModel(
                id=myid,
                JobTitle=JobTitle,
                CompanyName=CompanyName,
                Address=Address,
                CompanyDescription=CompanyDescription,
                JobDescription=JobDescription,
                Qualification=Qualification,
                SalaryInformation=SalaryInformation,
                Deadline=Deadline,
                Designation=Designation,
                Experience=Experience,
                Created_by=request.user
            )
        else:
            jobid=JobModel.objects.get(id=myid)
            job=JobModel(
            id=myid,
            JobTitle=JobTitle,
            CompanyName=CompanyName,
            Address=Address,
            CompanyDescription=CompanyDescription,
            JobDescription=JobDescription,
            Qualification=Qualification,
            SalaryInformation=SalaryInformation,
            Deadline=jobid.Deadline,
            Designation=Designation,
            Experience=Experience,
            Created_by=request.user
            )
        job.save()
        return redirect('dashboard')
    
@login_required
def viewsinglejob(request,myid):
    job=JobModel.objects.get(id=myid)
    jodDict={
        'job':job
    }
    return render(request,'viewsinglejob.html',jodDict)

@login_required
def profile(request):
    return render(request,'profile.html')





