from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    ProfilePicture=models.ImageField(upload_to='static/ProfilePic',null=True)
    FullName=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=100,null=True)
    PhoneNumber=models.CharField(max_length=100,null=True)
    EmailAddress=models.CharField(max_length=100,null=True)
    CareerObjective=models.TextField(null=True)
    HardSkills=models.CharField(max_length=100,null=True)
    SoftSkills=models.CharField(max_length=100,null=True)
    Certifications=models.CharField(max_length=100,null=True)
    Projects=models.CharField(max_length=100,null=True)
    References=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.FullName
    
class EducationModel(models.Model):
    Degree=models.CharField(max_length=100,null=True)
    Institution=models.CharField(max_length=100,null=True)
    GraduationYear=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.Institution
    
class WorkModel(models.Model):
    Company=models.CharField(max_length=100,null=True)
    Position=models.CharField(max_length=100,null=True)
    StartDate=models.CharField(max_length=100,null=True)
    EndDate =models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.Company