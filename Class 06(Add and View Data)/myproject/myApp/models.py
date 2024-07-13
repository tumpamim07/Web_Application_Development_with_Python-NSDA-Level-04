from django.db import models

class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    stdid=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)

    def __str__(self):
        return self.name+"-"+self.stdid+"-"+self.dept
    

class TeacherModel(models.Model):
    tecname=models.CharField(max_length=50)
    tecid=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self):
        return self.tecname+"-"+self.tecid+"-"+self.subject
