from django.db import models

class blogModel(models.Model):
    name11=models.CharField(max_length=20)
    blid=models.CharField(max_length=20)

    def __str__(self):
        return self.name11

class listModel(models.Model):
    name12=models.CharField(max_length=20)
    liid=models.CharField(max_length=20)


    def __str__(self):
        return self.name12
