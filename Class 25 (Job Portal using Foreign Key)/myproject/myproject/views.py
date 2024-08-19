from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def SignUppage(request):
    
    if request.method=='POST':
        displayname=request.POST.get('displayname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        email=request.POST.get('email')
        user_type=request.POST.get('user_type')
        
        if password==confirmpassword:
            user=Custome_User.objects.create_user(username=username,password=password)
            user.display_name=displayname
            user.email=email
            user.user_type=user_type
            user.save()
            return redirect("SignInpage")
    return render(request,'SignUppage.html')


def SignInpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            return redirect("dashboardPage")
        
        else:
            return redirect("SignInpage")
    return render(request,'SignInpage.html')

@login_required
def LogoutPage(request):
    logout(request)
    return redirect("SignInpage")


@login_required
def profile(request):
    
    return render(request,'profile.html')


@login_required
def dashboardPage(request):
    job=job_portal.objects.all()
    mydict={
        'job':job
    }
    return render(request,'dashboardPage.html',mydict)

@login_required
def addjob(request):
    if request.method=='POST':
       jobTitle=request.POST.get('jobTitle') 
       companyName=request.POST.get('companyName') 
       address=request.POST.get('address') 
       companyDescription=request.POST.get('companyDescription') 
       jobDescription=request.POST.get('jobDescription') 
       qualification=request.POST.get('qualification') 
       salary=request.POST.get('salary') 
       joiningDate=request.POST.get('joiningDate') 
       designation=request.POST.get('designation') 
       experience=request.POST.get('experience') 
       current_user=request.user
       
       addjob=job_portal(
           Job_title=jobTitle,
           company_name=companyName,
           address=address,
           company_description=companyDescription,
           job_description=jobDescription,
           qualification=qualification,
           salary=salary,
           joiningdate=joiningDate,
           designation=designation,
           experience=experience,
           created_by=current_user,
       )
       
       addjob.save()
       return redirect("joblist")
    return render(request,'recruiter/addjob.html')

@login_required
def joblist(request):
    lisst=job_portal.objects.all()
    mydict={
        'lisst':lisst
    }
    return render(request,'recruiter/joblist.html',mydict)

@login_required
def deletepage(request,id):
    delete=job_portal.objects.get(id=id)
    delete.delete()
    return redirect("joblist")


@login_required
def editpage(request,id):
    edits=job_portal.objects.filter(id=id)
    mydic={
        'edits':edits
    }
    return render(request,'recruiter/editpage.html',mydic)

@login_required
def updatepage(request):
    if request.method=='POST':
       id=request.POST.get('id') 
       jobTitle=request.POST.get('jobTitle') 
       companyName=request.POST.get('companyName') 
       address=request.POST.get('address') 
       companyDescription=request.POST.get('companyDescription') 
       jobDescription=request.POST.get('jobDescription') 
       qualification=request.POST.get('qualification') 
       salary=request.POST.get('salary') 
       joiningDate=request.POST.get('joiningDate') 
       designation=request.POST.get('designation') 
       experience=request.POST.get('experience') 
       
       
       addjob=job_portal(
           id=id,
           Job_title=jobTitle,
           company_name=companyName,
           address=address,
           company_description=companyDescription,
           job_description=jobDescription,
           qualification=qualification,
           salary=salary,
           joiningdate=joiningDate,
           designation=designation,
           experience=experience,
       )
       
       addjob.save()
    return redirect("joblist")



@login_required
def viewjob(request):
    return render(request,'seeker/viewjob.html')

@login_required
def viewpage(request,id):
    views=job_portal.objects.filter(id=id)
    mydic1={
        'views':views
    } 
    return render(request,'recruiter/viewpage.html',mydic1)
