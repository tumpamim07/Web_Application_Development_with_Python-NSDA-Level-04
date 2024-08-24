from django.db import models

class SocialMediaModel(models.Model):

    twitter=models.URLField(max_length=100,blank=True,null=True)
    facebook=models.URLField(max_length=100,blank=True,null=True)
    Instagram=models.URLField(max_length=100,blank=True,null=True)
    linkedin=models.URLField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.twitter
    

class AboutModel(models.Model):
    Profile_Picture = models.ImageField(upload_to='media/ProfilePic',null=True)
    Name=models.CharField(max_length=100,null=True)
    Profession1=models.CharField(max_length=100,null=True)
    Profession2=models.CharField(max_length=100,null=True)
    Profession3=models.CharField(max_length=100,null=True)
    Aboutdetails=models.CharField(max_length=500,null=True)
    ProfessionTitle1=models.CharField(max_length=100,null=True)
    ProfessionTitle2=models.CharField(max_length=100,null=True)
    ProfessionDetails=models.TextField(null=True)
    ProfessionPara=models.TextField(null=True)
    Birthday=models.CharField(max_length=100,null=True)
    Website=models.CharField(max_length=100,null=True)
    Phone=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    Age=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Status=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.Name
    
class ClientModel(models.Model):
    Fact=models.TextField(null=True)
    HappyClients=models.CharField(max_length=100,null=True)
    Projects=models.CharField(max_length=100,null=True)
    SuppotTime=models.CharField(max_length=100,null=True)
    HardWorkers=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.HappyClients
    
class SkillsModel(models.Model):
    Skills=models.TextField(null=True)
    
    def __str__(self):
        return self.Skills
    
class SkillMatricesModel(models.Model):
    SkillName=models.CharField(max_length=100,null=True)
    SkillProgress=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.SkillName
    
class ResumeModel(models.Model):
    Resume=models.TextField(null=True)
    Name=models.CharField(max_length=100,null=True)
    About=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=100,null=True)
    Mobile=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.Name  

class ResumeEducationModel(models.Model):
    EducationName=models.CharField(max_length=100,null=True)
    EducationYear=models.CharField(max_length=100,null=True)
    EducationInstitute=models.CharField(max_length=100,null=True)
    EducationDetails=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.EducationName
    
class ResumeProExModel(models.Model):
    ProfessionName=models.CharField(max_length=100,null=True)
    ProfessionalYear=models.CharField(max_length=100,null=True)
    ProfessionalLocation=models.CharField(max_length=100,null=True)
    ProfessionalResponsibilities=models.TextField(null=True)

    def __str__(self):
        return self.ProfessionName

class PortfolioModel(models.Model):
    Portfolio=models.TextField(null=True)
    
    def __str__(self):
        return self.Portfolio
    
class ServicesModel(models.Model):
    Services=models.TextField(null=True)

    def __str__(self):
        return self.Services

class ServicesSectionModel(models.Model):
    Icon=models.CharField(max_length=100,null=True)
    ServiceName=models.CharField(max_length=100,null=True)
    ServiceDetails=models.TextField(null=True)
    
    def __str__(self):
        return self.ServiceName
    
class TestimonialModel(models.Model):
    Testimonial=models.TextField(null=True)
    
    def __str__(self):
        return self.Testimonial

class ClientTestimonialModel(models.Model):
    ClientName=models.CharField(max_length=100,null=True)
    ClientPic=models.ImageField(upload_to='media/ClientPic',null=True)
    ClientProfession=models.CharField(max_length=100,null=True)
    ClientReview=models.TextField(null=True)

    def __str__(self):
        return self.ClientName

class ContactModel(models.Model):
    ContactDetails=models.TextField(null=True)
    ContactLocation=models.CharField(max_length=100,null=True)
    ContactEmail=models.CharField(max_length=100,null=True)
    ContactCall=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.ContactDetails