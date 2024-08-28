from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    USER=[
        ('chef','Chef'),('viewer','Viewer')
    ]
    GENDER=[
        ('male','Male'),('female','Female')
    ]
    usertype=models.CharField(choices=USER,max_length=50)
    gender=models.CharField(choices=GENDER,max_length=50)
    age=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

class RecipeModel(models.Model):
    DIFFICULTY=[
        ('high','High'),
        ('medium','Medium'),
        ('low','Low')
    ]
    CATEGORY=[
        ('breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('dinner','Dinner')
    ]
    TAGS=[
        ('vegetarian','Vegetarian'),
        ('nonvegetarian','NonVegetarian'),
    ]
    
    difficulty_level=models.CharField(choices=DIFFICULTY,max_length=50,null=True)
    recipe_category=models.CharField(choices=CATEGORY,max_length=50,null=True)
    tags=models.CharField(choices=TAGS,max_length=50,null=True)
    recipe_title=models.CharField(max_length=50,null=True)
    ingredients=models.CharField(max_length=50,null=True)
    instruction=models.CharField(max_length=50,null=True)
    prep_time=models.CharField(max_length=50,null=True)
    cooking_time=models.CharField(max_length=50,null=True)
    total_time=models.CharField(max_length=50,null=True)
    nutritional_info=models.CharField(max_length=50,null=True)
    sample_image=models.ImageField(upload_to="static/RecipeImage",null=True)
    total_calories=models.CharField(max_length=50,null=True)
    created_by=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)

class chefProfile(models.Model):
    myUser=models.OneToOneField(UserModel,on_delete=models.CASCADE,null=True)
    experience=models.CharField(max_length=50,null=True)
    skills=models.CharField(max_length=50,null=True)
    resume=models.CharField(max_length=50,null=True)
    Profile_Picture=models.ImageField(upload_to="static/Profile_Picture",null=True)

    def __str__(self):
        return self.myUser.usertype
    
class ViewerProfile(models.Model):
    myUser=models.OneToOneField(UserModel,on_delete=models.CASCADE,null=True)
    Profile_Picture=models.ImageField(upload_to="static/Profile_Picture",null=True)
    Favourite=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.myUser.username