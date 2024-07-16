from django.db import models

class StudentModel(models.Model):
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=50,null=True)
    Country=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.FirstName+"-"+self.LastName
