from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')



def about(request):
    data="get all data from database"
    return HttpResponse(data)

def contact(request):
    return HttpResponse("This is our contact page")