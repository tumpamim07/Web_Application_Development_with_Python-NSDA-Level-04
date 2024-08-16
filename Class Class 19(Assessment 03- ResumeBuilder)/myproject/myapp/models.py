from django.db import models

class resumeModel(models.Model):
    Profilepicture=models.ImageField(upload_to="resume/ProfilePicture",null=True)
    FullName=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    PhoneNumber=models.CharField(max_length=50,null=True)
    EmailAddress=models.CharField(max_length=50,null=True)
    CareerObjective=models.TextField(null=True)
    Certifications=models.TextField(null=True)
    Projects=models.CharField(max_length=50,null=True)
    References=models.CharField(max_length=50,null=True)

    #education
    Degree=models.CharField(max_length=50,null=True)
    Institution=models.CharField(max_length=50,null=True)
    Graduationyear=models.CharField(max_length=50,null=True)
    
    #work
    Company=models.CharField(max_length=50,null=True)
    Position=models.CharField(max_length=50,null=True)
    StartDate=models.CharField(max_length=50,null=True)
    EndDate=models.CharField(max_length=50,null=True)

    #skill
    SoftSkills=models.CharField(max_length=50,null=True)
    HardSkills=models.CharField(max_length=50,null=True)
