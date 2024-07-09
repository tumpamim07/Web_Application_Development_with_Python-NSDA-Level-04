from django.shortcuts import render,redirect,HttpResponse

def Homepage(request):
    return HttpResponse("Hello")

def Contact(request):
    return HttpResponse(123456789)

def About(request):
    return HttpResponse("About Us")

def Location(request):
    return HttpResponse("Our Location")

def Follow(request):
    return HttpResponse("Follow Us")

