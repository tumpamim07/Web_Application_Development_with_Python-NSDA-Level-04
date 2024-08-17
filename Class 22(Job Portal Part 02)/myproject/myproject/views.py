from django.shortcuts import render,redirect
from myapp.models import *


def SigninPage(request):
    return render(request,'SigninPage.html')

def SignupPage(request):

    if request.method=='POST':
        image=request.FILES.get('image')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        gender=request.POST.get('gender')
        blood=request.POST.get('blood')
        email=request.POST.get('email')
        usertype=request.POST.get('usertype')
        displayname=request.POST.get('displayname')
        
        if pass_word==confirmpassword:
            user=Customet_User.objects.create_user(username=user_name,password=pass_word)
            user.Image=image
            user.firstname=firstname
            user.lastname=lastname
            user.DOB=dob
            user.Address=address
            user.Gender=gender
            user.Blood=blood
            user.user_typr=usertype
            user.display_name=displayname
            user.email=email
            user.save()
            return redirect('SigninPage')
        else:
            return redirect ('SignupPage')
    return render(request,'SignupPage.html')