from django.db import models

class StudentModel(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Roll=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=50,null=True)
    Image=models.ImageField(upload_to="media/Student_Image",null=True)

    def __str__(self):
        return self.Name
    
