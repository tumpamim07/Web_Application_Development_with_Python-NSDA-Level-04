from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),('jobseeker','JobSeeker')
    ]
    
    display_name=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    user_type=models.CharField(choices=USER,max_length=100)
    
    def __str__(self):
        return self.user_name
