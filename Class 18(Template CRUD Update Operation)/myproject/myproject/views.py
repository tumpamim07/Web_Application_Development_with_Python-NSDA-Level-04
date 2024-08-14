from django.shortcuts import render,redirect,HttpResponse
from myapp.models import *


def index(request):
    socialmedia=SocialMediaModel.objects.get()
    about=AboutModel.objects.get()
    client=ClientModel.objects.get()
    skills=SkillsModel.objects.get()
    skillmat=SkillMatricesModel.objects.all()
    resume=ResumeModel.objects.get()
    resumeedu=ResumeEducationModel.objects.all()
    resumepro=ResumeProExModel.objects.all()
    portfolio=PortfolioModel.objects.get()
    service=ServicesModel.objects.get()
    servicesect=ServicesSectionModel.objects.all()
    testimonial=TestimonialModel.objects.get()
    clienttestimonial=ClientTestimonialModel.objects.all()
    contact=ContactModel.objects.get()
    mydict={
        'socialmedia':socialmedia,
        'about':about,
        'client':client,
        'skills':skills,
        'skillmat':skillmat,
        'resume':resume,
        'resumeedu':resumeedu,
        'resumepro':resumepro,
        'portfolio':portfolio,
        'service':service,
        'servicesect':servicesect,
        'testimonial':testimonial,
        'clienttestimonial':clienttestimonial,
        'contact':contact,
    }
    return render(request,'index.html',mydict)

def editabout(request,myid):
    about = AboutModel.objects.get(id=myid)
    mydict={
        'about':about
    }
    return render(request,'editabout.html',mydict)


def updateabout(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        Profile_Picture=request.FILES.get('Profile_Picture')
        Name=request.POST.get('Name')
        Profession1=request.POST.get('Profession1')
        Profession2=request.POST.get('Profession2')
        Profession3=request.POST.get('Profession3')
        Aboutdetails=request.POST.get('Aboutdetails')
        ProfessionTitle1=request.POST.get('ProfessionTitle1')
        ProfessionTitle2=request.POST.get('ProfessionTitle2')
        ProfessionDetails=request.POST.get('ProfessionDetails')
        ProfessionPara=request.POST.get('ProfessionPara')
        Birthday=request.POST.get('Birthday')
        Website=request.POST.get('Website')
        Phone=request.POST.get('Phone')
        City=request.POST.get('City')
        Age=request.POST.get('Age')
        Email=request.POST.get('Email')
        Status=request.POST.get('Status')
        if Profile_Picture:  
            about=AboutModel(
                id=myid,
                Profile_Picture=Profile_Picture,
                Name=Name,
                Profession1=Profession1,
                Profession2=Profession2,
                Profession3=Profession3,
                Aboutdetails=Aboutdetails,
                ProfessionTitle1=ProfessionTitle1,
                ProfessionTitle2=ProfessionTitle2,
                ProfessionDetails=ProfessionDetails,
                ProfessionPara=ProfessionPara,
                Birthday=Birthday,
                Website=Website,
                Phone=Phone,
                City=City,
                Age=Age,
                Email=Email,
                Status=Status,
            )
        else:
            aboutid=AboutModel.objects.get(id=myid)
            about=AboutModel(
                id=myid,
                Profile_Picture=aboutid.Profile_Picture,
                Name=Name,
                Profession1=Profession1,
                Profession2=Profession2,
                Profession3=Profession3,
                Aboutdetails=Aboutdetails,
                ProfessionTitle1=ProfessionTitle1,
                ProfessionTitle2=ProfessionTitle2,
                ProfessionDetails=ProfessionDetails,
                ProfessionPara=ProfessionPara,
                Birthday=Birthday,
                Website=Website,
                Phone=Phone,
                City=City,
                Age=Age,
                Email=Email,
                Status=Status,
            )
        about.save()
        return redirect('/')