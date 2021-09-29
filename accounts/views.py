from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import smtplib
import os
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
        mg = request.POST['message']
        

         # get email and password from environment variables
    
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    
    # set up email content
        msg = EmailMessage()
        msg['Subject'] = 'Alpha Trip'
        msg['From'] = thealphadebuggers@gmail.com
        msg['To'] = email
        msg.set_content(f"Hi {username}! We will look into your message and send you a reply as soon as possible if needed. Thank you for using Alpha Trip! Your message: {mg}")
    
    # send email
         with s.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(thealphadebuggers@gmail.com, EMAIL_PASSWORD)
            smtp.send_message(msg)
            
            s.quit()
        

      
    return redirect('/')
  else:
        return render(request,'contact.html')
        return redirect('contact')
 





    
