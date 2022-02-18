from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully.')


    return render(request,'contact.html')

def signup(request):
    if request.method == "POST":
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       rpassword=request.POST['rpassword']

       if password == rpassword:
          if User.objects.filter(email=email).exists():
              messages.info(request, 'Email already used')
              return redirect('signup')
          else:
             user=User.objects.create_user(username=username, email=email, password=password)
             user.save();
             return redirect('login')
       else:
         messages.info(request, 'Password not same ')
         return redirect('signup')
    else:
      return render(request,'signup.html')

def login(request):
    return render(request,'login.html')