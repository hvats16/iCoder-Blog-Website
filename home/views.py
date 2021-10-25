from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User


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

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def handlesignup(request):
    if request.method == 'POST':
        # Get the Post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Check for errorneous input
        if len(username) > 10:
            messages.success(request,"Your Username must be under 10 characters")
            return redirect('/')
        
        if not username.isalnum():
            messages.success(request,"Your Username should only contain letter and numbers ")
            return redirect('/')
            
        if pass1 != pass2:
            messages.success(request,"Password do not match")
            return redirect('/')




        #create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your iCoder account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not Found")
