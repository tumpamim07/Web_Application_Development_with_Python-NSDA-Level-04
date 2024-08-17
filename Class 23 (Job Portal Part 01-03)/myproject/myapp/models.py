from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('job_seeker','Job_Seeker'),('job_recruiter','Job_Recruiter')
    ]
    GENDER=[
        ('female','Female'),('male','Male')
    ]
    BLOOD=[
        ('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('ab+','AB+'),('ab-','AB-'),('o+','O+'),('o-','O-'),
    ]
    user_type=models.CharField(choices=USER,max_length=50,null=True)
    gender=models.CharField(choices=GENDER,max_length=50,null=True)
    blood=models.CharField(choices=BLOOD,max_length=50,null=True)
    display_name=models.CharField(max_length=50,null=True)
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    address=models.TextField(max_length=50,null=True)
    DOB=models.DateField(max_length=50,null=True)
    Image=models.ImageField(upload_to="Project_image/image",null=True)
    
class JobModel(models.Model):
    JobTitle=models.CharField(max_length=50,null=True)
    CompanyName=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    CompanyDescription=models.TextField(null=True)
    JobDescription=models.TextField(null=True)
    Qualification=models.CharField(max_length=50,null=True)
    SalaryInformation=models.CharField(max_length=50,null=True)
    Deadline=models.DateField(null=True)
    Designation=models.CharField(max_length=50,null=True)
    Experience=models.CharField(max_length=50,null=True)
    

    
    
