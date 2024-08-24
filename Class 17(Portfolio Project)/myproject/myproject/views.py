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
