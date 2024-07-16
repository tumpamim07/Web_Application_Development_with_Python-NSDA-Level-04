from django.db import models

class StudentModel(models.Model):
    StudentName=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)
    StudentImage=models.ImageField(upload_to="media/Student_Image",null=True)

    def __str__(self):
        return self.StudentName
    
class TeacherModel(models.Model):
    TeacherName=models.CharField(max_length=50,null=True)
    TDepartment=models.CharField(max_length=50,null=True)
    TCity=models.CharField(max_length=50,null=True)
    TImage=models.ImageField(upload_to="media/Teacher_Image", null=True)

    def __str__(self):
        return self.TeacherName
    
class DoctorModel(models.Model):
    DoctorName=models.CharField(max_length=50,null=True)
    DDepartment=models.CharField(max_length=50,null=True)
    DCity=models.CharField(max_length=50,null=True)
    DImage=models.ImageField(upload_to="media/Doctor_Image",null=True)

    def __str__(self):
        return self.DoctorName
