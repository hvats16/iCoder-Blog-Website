from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

def blogHome(request):
    return HttpResponse("We will keep all the post here")

def blogPost(request,slug): 
    return HttpResponse(f'This is blog: {slug} ')
