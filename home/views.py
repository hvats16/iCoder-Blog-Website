from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages


def home(request): 
    return render(request, 'home/home.html')


def about(request): 
    return render(request, 'home/about.html')

def contact(request):
    messages.success(request, 'Welcome to Contact')
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name,email=email,phone=phone,content=content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            messages.success(request, "Your form has been submitted")
        contact.save()
    return render(request, "home/contact.html")

    def __str__(self):
        return 'Message from' + self.name