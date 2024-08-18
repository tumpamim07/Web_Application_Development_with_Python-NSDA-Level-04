from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to='media/profile_pic')
    date_of_birth=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=100)
    BLOOD_GROUP=[
        ('a+','A Positive'),
        ('a-','A Negative'),
        ('b+','B Positive'),
        ('b-','B Negative'),
        ('ab+','AB Positive'),
        ('ab-','AB Negative'),
        ('o+','O Positive'),
        ('o-','O Negative'),
    ]
    blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
    USER_TYPE=[
        ('recruiter','Job Recruiter'),
        ('seeker','Job Seeker'),
    ]
    user_type=models.CharField(choices=USER_TYPE,max_length=100)
    
    def __str__(self):
        return self.fname
    
class JobModel(models.Model):
    Recruiter=models.CharField(max_length=100)
    Job_title=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Company_description=models.TextField()
    Job_description=models.TextField()
    Qualification=models.CharField(max_length=100)
    Salary_information=models.CharField(max_length=100)
    Deadline=models.DateField(auto_now_add=True)
    Designation=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Job_title
