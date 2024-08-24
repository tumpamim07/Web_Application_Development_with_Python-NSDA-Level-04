from django.db import models
from django.contrib.auth.models import AbstractUser


class Custom_User_Model(AbstractUser):
    profilePicture=models.ImageField(upload_to='static/profilepic',null=True)
    dob=models.DateField(null=True)
    address=models.TextField(null=True)
    
    BLOOD=[
        ('a+','A+'),
        ('a-','A-'),
        ('b+','B+'),
        ('b-','B-'),
        ('ab+','AB+'),
        ('ab-','AB-'),
        ('o+','O+'),
        ('o-','O-'),
    ]

    bloodGroup=models.CharField(choices=BLOOD,max_length=100,null=True)

    USER_TYPE=[
        ('recruiter','Job Recruiter'),
        ('seeker','Job Seeker'),
    ]

    usertype=models.CharField(choices=USER_TYPE,max_length=100,null=True)
    
    def __str__(self):
        return self.username

class JobModel(models.Model):
    JobTitle=models.CharField(max_length=100,null=True)
    CompanyName=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=100,null=True)
    CompanyDescription=models.TextField(null=True)
    JobDescription=models.TextField(null=True)
    Qualification=models.CharField(max_length=100,null=True)
    SalaryInformation=models.CharField(max_length=100,null=True)
    Deadline=models.DateField(null=True)
    Designation=models.CharField(max_length=100,null=True)
    Experience=models.CharField(max_length=100,null=True)
    Created_by=models.ForeignKey(Custom_User_Model,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.Job_title} created by {self.Created_by}"