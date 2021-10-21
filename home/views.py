from django.shortcuts import render, HttpResponse


def home(request): 
    return HttpResponse('This is home ')

def contact(request):
    return HttpResponse("This is contact")

def about(request): 
    return HttpResponse('This is about')