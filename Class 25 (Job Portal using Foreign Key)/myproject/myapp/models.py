from django.db import models
from django.contrib.auth.models import AbstractUser

class Custome_User(AbstractUser):
    USER=[
        ('job_recruiter','Job_Recruiter'),('job_seeker','Job_Seeker')
    ]
    display_name=models.CharField(max_length=50)
    user_type=models.CharField(choices=USER,max_length=50)
    
class job_portal(models.Model):
    Job_title=models.CharField(max_length=50,null=True)
    company_name=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    company_description=models.CharField(max_length=50,null=True)
    job_description=models.CharField(max_length=50,null=True)
    qualification=models.CharField(max_length=50,null=True)
    salary=models.CharField(max_length=50,null=True)
    joiningdate=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=50,null=True)
    experience=models.CharField(max_length=50,null=True)
    created_by=models.ForeignKey(Custome_User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Job_title+"is Created by "+self.created_by.display_name