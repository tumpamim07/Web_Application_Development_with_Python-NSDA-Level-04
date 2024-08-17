from django.shortcuts import render,redirect

def SignupPage(request):
    return render (request,'SignupPage.html')

def SigninPage(request):
    return render (request,'SigninPage.html')