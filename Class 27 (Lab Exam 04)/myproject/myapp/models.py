from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
    ]
    gender=models.CharField(choices=GENDER,max_length=50,null=True)
    age=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)

    USER_TYPE=[
        ('chef','Chef'),
        ('viewer','Viewer'),
    ]
    usertype=models.CharField(choices=USER_TYPE,max_length=50,null=True)

    def __str__(self):
        return self.username
    
class RecipeModel(models.Model):
    RecipeTitle=models.CharField(max_length=100,null=True)
    Ingredients=models.TextField(null=True)
    Instructions=models.TextField(null=True)
    PreparationTime=models.CharField(max_length=100,null=True)
    CookingTime=models.CharField(max_length=100,null=True)
    TotalTime=models.CharField(max_length=100,null=True)
    
    DIFFICULTY_LEVEL=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]
    
    DifficultyLevel=models.CharField(choices=DIFFICULTY_LEVEL,max_length=50,null=True)
    NutritionalInfo=models.TextField(null=True)
    RecipeImage=models.ImageField(upload_to='static/recipeimage',null=True)
    RECIPE_CATEGORY=[
        ('breakfast','Breakfast'),
        ('launch','Launch'),
        ('dinner','Dinner'),
    ]
    RecipeCategory=models.CharField(choices=RECIPE_CATEGORY,max_length=50,null=True)

    USER_TAGS=[
        ('vegetarian','Vegetarian'),
        ('non-vegetarian','Non Vegetarian'),
    ]
    UserTags=models.CharField(choices=USER_TAGS,max_length=50,null=True)
    TotalCalorie=models.CharField(max_length=40,null=True)
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.RecipeTitle} created by {self.created_by}"