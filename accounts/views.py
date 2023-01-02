from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
import smtplib
import os
from os import environ
# Create your views here.


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')

    else:
        return render(request,'login.html')
        return redirect('login')
        

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
              user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
              user.save();
              print('User created')
              return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')

    else:
    
       return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    
      
  if request.method== 'POST':
        email = request.POST['email']
        username = request.POST['username']
        msg = request.POST['message']
        
        #Email_Password = os.environ.get('Email_Password')

        send_mail(
       'AlphaTrip',  # Subject
       f"Hi {username}! Thank you for visiting AlphaTrip. Keep Exploring!",  # Message
       'thealphadebuggers@gmail.com',  # From email
       [f"{email}"],  # List of recipient email addresses
       fail_silently=False,  # Optional argument to suppress errors
       )

        send_mail(
       'AlphaTrip',  # Subject
       f"Using the email address {email}, here is a message from {username}: {msg}. From AlphaTrip Website.",  # Message
       'thealphadebuggers@gmail.com',  # From email
       ['thealphadebuggers@gmail.com'],  # List of recipient email addresses
       fail_silently=False,  # Optional argument to suppress errors
       )

        s.quit()
        

      
        return redirect('/')
  else:
        return render(request,'contact.html')
        return redirect('contact')
 





    
