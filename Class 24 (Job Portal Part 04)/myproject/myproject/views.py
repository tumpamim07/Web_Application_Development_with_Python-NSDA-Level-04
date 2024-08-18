from django.shortcuts import render,redirect
from myapp.models import CustomUserModel,JobModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        profile_picture=request.FILES.get('profile_picture')
        date_of_birth=request.POST.get('date_of_birth')
        address=request.POST.get('address')
        blood_group=request.POST.get('blood_group')
        user_type=request.POST.get('user_type')
        
        if password==confirm_password:
            user=CustomUserModel.objects.create_user(
                username=uname,
                password=password,
            )
            user.email=email
            user.fname=firstname
            user.lname=lastname
            user.lname=lastname
            user.profile_picture=profile_picture
            user.date_of_birth=date_of_birth
            user.address=address
            user.blood_group=blood_group
            user.user_type=user_type
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')

    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        
        user = authenticate(
            username=uname,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')
    return render(request,'signin.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def dashboard(request):
    job=JobModel.objects.all()
    jobDict={
        'job':job
    }
    return render(request,'dashboard.html',jobDict)

@login_required
def addjob(request):
    if request.user.user_type == 'recruiter':
        if request.method=="POST":
            Job_title=request.POST.get('Job_title')
            Company_name=request.POST.get('Company_name')
            Address=request.POST.get('Address')
            Company_description=request.POST.get('Company_description')
            Job_description=request.POST.get('Job_description')
            Qualification=request.POST.get('Qualification')
            Salary_information=request.POST.get('Salary_information')
            Deadline=request.POST.get('Deadline')
            Designation=request.POST.get('Designation')
            Experience=request.POST.get('Experience')
            
            job=JobModel(
                Recruiter=request.user.username,
                Job_title=Job_title,
                Company_name=Company_name,
                Address=Address,
                Company_description=Company_description,
                Job_description=Job_description,
                Qualification=Qualification,
                Salary_information=Salary_information,
                Deadline=Deadline,
                Designation=Designation,
                Experience=Experience,
            )
            job.save()
            return redirect('viewjob')
        return render(request,'recruiter/addjob.html')
    else:
        logout(request)
        return redirect('signin')

@login_required
def viewjob(request):
    job=JobModel.objects.all()
    jobDict={
        'jobs':job
    }
    return render(request,'viewjob.html',jobDict)
@login_required
def deletejob(request,myid):
    job=JobModel.objects.get(id=myid)
    job.delete()
    return redirect('viewjob')
@login_required
def editjob(request,myid):
    job=JobModel.objects.get(id=myid)
    jobDict={
        'jobs':job
    }
    return render(request,'editjob.html',jobDict)
@login_required
def updatejob(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        Job_title=request.POST.get('Job_title')
        Company_name=request.POST.get('Company_name')
        Address=request.POST.get('Address')
        Company_description=request.POST.get('Company_description')
        Job_description=request.POST.get('Job_description')
        Qualification=request.POST.get('Qualification')
        Salary_information=request.POST.get('Salary_information')
        Deadline=request.POST.get('Deadline')
        Designation=request.POST.get('Designation')
        Experience=request.POST.get('Experience')
        
        if Deadline:

            job=JobModel(
                id=myid,
                Recruiter=request.user.username,
                Job_title=Job_title,
                Company_name=Company_name,
                Address=Address,
                Company_description=Company_description,
                Job_description=Job_description,
                Qualification=Qualification,
                Salary_information=Salary_information,
                Deadline=Deadline,
                Designation=Designation,
                Experience=Experience,
            )
        else:
            jobbyid=JobModel.objects.get(id=myid)
            job=JobModel(
                id=myid,
                Recruiter=request.user.username,
                Job_title=Job_title,
                Company_name=Company_name,
                Address=Address,
                Company_description=Company_description,
                Job_description=Job_description,
                Qualification=Qualification,
                Salary_information=Salary_information,
                Deadline=jobbyid.Deadline,
                Designation=Designation,
                Experience=Experience,
            )
        job.save()
    return redirect('viewjob')