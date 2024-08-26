from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        usertype=request.POST.get('usertype')

        if password==confirmpassword:
            user=CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                gender=gender,
                age=age,
                city=city,
                country=country,
                usertype=usertype,
            )
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'signin.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def dashboard(request):
    current_user=request.user
    if current_user.usertype=='chef':
        recipe=RecipeModel.objects.filter(created_by=current_user)
    else:
        recipe=RecipeModel.objects.all()
    mydict={
        'recipe':recipe
    }
    return render(request,'dashboard.html',mydict)

@login_required
def addrecipe(request):
    if request.method=="POST":
        RecipeTitle=request.POST.get('RecipeTitle')
        Ingredients=request.POST.get('Ingredients')
        Instructions=request.POST.get('Instructions')
        PreparationTime=request.POST.get('PreparationTime')
        CookingTime=request.POST.get('CookingTime')
        TotalTime=request.POST.get('TotalTime')
        DifficultyLevel=request.POST.get('DifficultyLevel')
        NutritionalInfo=request.POST.get('NutritionalInfo')
        RecipeImage=request.FILES.get('RecipeImage')
        RecipeCategory=request.POST.get('RecipeCategory')
        UserTags=request.POST.get('UserTags')
        TotalCalorie=request.POST.get('TotalCalorie')

        recipe=RecipeModel(
            RecipeTitle=RecipeTitle,
            Ingredients=Ingredients,
            Instructions=Instructions,
            PreparationTime=PreparationTime,
            CookingTime=CookingTime,
            TotalTime=TotalTime,
            DifficultyLevel=DifficultyLevel,
            NutritionalInfo=NutritionalInfo,
            RecipeImage=RecipeImage,
            RecipeCategory=RecipeCategory,
            UserTags=UserTags,
            TotalCalorie=TotalCalorie,
            created_by=request.user,
        )
        recipe.save()
        return redirect('dashboard')
    return render(request,'chef/addrecipe.html')

@login_required
def deleterecipe(request,myid):
    recipe=RecipeModel.objects.get(id=myid)
    recipe.delete()
    return redirect('dashboard')

@login_required
def viewallrecipe(request):
    current_user=request.user
    if current_user.usertype=='chef':
        recipes=RecipeModel.objects.filter(created_by=current_user)
    else:
        recipes=RecipeModel.objects.all()
    mydict={
        'recipes':recipes
    }
    return render(request,'viewallrecipe.html',mydict)

@login_required
def singlerecipeview(request,myid):
    recipes=RecipeModel.objects.get(id=myid)
    mydict={
        'recipe':recipes
    }
    return render(request,'singlerecipeview.html',mydict)


@login_required
def editrecipe(request,myid):
    recipes=RecipeModel.objects.get(id=myid)
    mydict={
        'recipe':recipes
    }
    return render(request,'chef/editrecipe.html',mydict)


@login_required
def udpaterecipe(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        RecipeTitle=request.POST.get('RecipeTitle')
        Ingredients=request.POST.get('Ingredients')
        Instructions=request.POST.get('Instructions')
        PreparationTime=request.POST.get('PreparationTime')
        CookingTime=request.POST.get('CookingTime')
        TotalTime=request.POST.get('TotalTime')
        DifficultyLevel=request.POST.get('DifficultyLevel')
        NutritionalInfo=request.POST.get('NutritionalInfo')
        RecipeImage=request.FILES.get('RecipeImage')
        RecipeCategory=request.POST.get('RecipeCategory')
        UserTags=request.POST.get('UserTags')
        TotalCalorie=request.POST.get('TotalCalorie')

        if RecipeImage:
            recipe=RecipeModel(
                id=myid,
                RecipeTitle=RecipeTitle,
                Ingredients=Ingredients,
                Instructions=Instructions,
                PreparationTime=PreparationTime,
                CookingTime=CookingTime,
                TotalTime=TotalTime,
                DifficultyLevel=DifficultyLevel,
                NutritionalInfo=NutritionalInfo,
                RecipeImage=RecipeImage,
                RecipeCategory=RecipeCategory,
                UserTags=UserTags,
                TotalCalorie=TotalCalorie,
                created_by=request.user,
            )
        else:
            recipeid=RecipeModel.objects.get(id=myid)
            recipe=RecipeModel(
                id=myid,
                RecipeTitle=RecipeTitle,
                Ingredients=Ingredients,
                Instructions=Instructions,
                PreparationTime=PreparationTime,
                CookingTime=CookingTime,
                TotalTime=TotalTime,
                DifficultyLevel=DifficultyLevel,
                NutritionalInfo=NutritionalInfo,
                RecipeImage=recipeid.RecipeImage,
                RecipeCategory=RecipeCategory,
                UserTags=UserTags,
                TotalCalorie=TotalCalorie,
                created_by=request.user,
            )
        recipe.save()
    return redirect('dashboard')