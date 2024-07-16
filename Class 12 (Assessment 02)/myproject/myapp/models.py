from django.db import models

class CandidateModel(models.Model):
    
    full_name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone_number=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    job_title=models.CharField(max_length=50,null=True)
    linkedin_profile=models.CharField(max_length=50,null=True)
    university=models.CharField(max_length=50,null=True)
    degree=models.CharField(max_length=50,null=True)
    languages=models.CharField(max_length=50,null=True)
    years_of_experience=models.CharField(max_length=50,null=True)
    
