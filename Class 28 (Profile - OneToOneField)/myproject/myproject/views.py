from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def SigninPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("dashboard")
        else:
            return redirect("SigninPage")

    return render(request,'SigninPage.html')

def SignUpPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        usertype=request.POST.get('usertype')

        if password==confirm_password:
            user=UserModel.objects.create_user(username=username,password=password)
            user.email=email
            user.gender=gender
            user.age=age
            user.city=city
            user.country=country
            user.usertype=usertype
            user.save()
            return redirect("SigninPage")
        else:
            return redirect("SignUpPage")
    return render(request,'SignUpPage.html')
@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def Logoutpage(request):
    logout(request)
    return redirect("SigninPage")

@login_required
def addrecipe(request):
    if request.method=="POST":
        recipe_title=request.POST.get('recipe_title')
        ingredients=request.POST.get('ingredients')
        instruction=request.POST.get('instruction')
        prep_time=request.POST.get('prep_time')
        cooking_time=request.POST.get('cooking_time')
        total_time=request.POST.get('total_time')
        difficulty_level=request.POST.get('difficulty_level')
        nutritional_info=request.POST.get('nutritional_info')
        sample_image=request.FILES.get('sample_image')
        recipe_category=request.POST.get('recipe_category')
        tags=request.POST.get('tags')
        total_calories=request.POST.get('total_calories')

        curruent_user=request.user

        recipee=RecipeModel(
            recipe_title=recipe_title,
            ingredients=ingredients,
            instruction=instruction,
            prep_time=prep_time,
            cooking_time=cooking_time,
            total_time=total_time,
            difficulty_level=difficulty_level,
            nutritional_info=nutritional_info,
            sample_image=sample_image,
            recipe_category=recipe_category,
            tags=tags,
            total_calories=total_calories,
            created_by=curruent_user,
        )
        recipee.save()
        return redirect("recipelist")
    return render(request,'chef/addrecipe.html')


@login_required
def recipelist(request):
    current_user=request.user

    if current_user.usertype == 'chef':
        recipee=RecipeModel.objects.filter(created_by=current_user)
        mydict={
            'recipee':recipee
        }
    return render(request,'chef/recipelist.html',mydict)


@login_required
def viewpage(request,id):
    recipee=RecipeModel.objects.filter(id=id)
    mydict={
        'recipee':recipee
    }

    return render(request,'chef/viewpage.html',mydict)


@login_required
def profile(request):

    viewer=ViewerProfile.objects.all()
    chef=chefProfile.objects.all()
    mydict={
        'viewer':viewer,
        'chef':chef
    }
    return render(request,'profile.html',mydict)


@login_required
def viewrecipe(request):
    recipee=RecipeModel.objects.all()
    mydict={
        'recipee':recipee
    }
    
    return render(request,'viewer/viewrecipe.html',mydict)