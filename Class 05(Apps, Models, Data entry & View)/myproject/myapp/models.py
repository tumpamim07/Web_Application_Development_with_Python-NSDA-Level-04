from django.db import models

class studentModel(models.Model):
    name=models.CharField(max_length=50)
    stdid=models.CharField(max_length=20)

    def __str__(self):
        return self.name+"-"+self.stdid

class teacherModel(models.Model):
    name1=models.CharField(max_length=50)
    tchid=models.CharField(max_length=50)

    def __str__(self):
        return self.name1
    
class workerModel(models.Model):
    name2=models.CharField(max_length=20)
    workid=models.CharField(max_length=20)

    def __str__(self):
        return self.name2
    
class subjectModel(models.Model):
    name3=models.CharField(max_length=20)
    subid=models.CharField(max_length=20)

    def __str__(self):
        return self.name3
    
class classModel(models.Model):
    name4=models.CharField(max_length=20)
    classid=models.CharField(max_length=50)

    def __str__(self):
        return self.name4