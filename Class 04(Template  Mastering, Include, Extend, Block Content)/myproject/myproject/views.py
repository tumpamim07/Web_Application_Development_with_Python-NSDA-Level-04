from django.shortcuts import render,redirect,HttpResponse

def Base(request):
    return render(request,'Base.html')

def Home(request):
    return render(request,'Home.html')

def News(request):
    return render(request,'News.html')

def Contact(request):
    return render(request,'Contact.html')

def About(request):
    return render(request,'About.html')

def Location(request):
    return render(request,'Location.html')