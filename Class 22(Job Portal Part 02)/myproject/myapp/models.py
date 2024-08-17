from django.db import models
from django.contrib.auth.models import AbstractUser


class Customet_User(AbstractUser):
    USER=[
        ('jobrecruiter','JobRecuiter'),('jobseeker','JobSeeker')
    ]

    BLOOD=[
        ('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('ab+','AB+'),('ab-','AB-'),('o+','O+'),('o-','O-')
    ]
    GENDER=[
        ('female','Female'),('male','Male')
    ]
    user_typr=models.CharField(choices=USER,max_length=50,null=True)
    display_name=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    DOB=models.DateField(max_length=50,null=True)
    Blood=models.CharField(choices=BLOOD,max_length=50,null=True)
    Gender=models.CharField(choices=GENDER,max_length=50,null=True)
    Image=models.ImageField(upload_to="Jobportal/image",null=True)