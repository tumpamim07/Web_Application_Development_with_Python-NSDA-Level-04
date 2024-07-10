from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def table(request):
    mydict={
        'Name':'Tumpa',
        'Department':'CSE',
        'Semester':'5th',
        'Name1':'Urmi',
        'Department1':'CSE',
        'Semester1':'5th',
    }
    return render(request,'table.html',mydict)