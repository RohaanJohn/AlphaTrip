from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import smtplib
# Create your views here.
Email_Password = os.environ.get('Email_Password')

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

        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("thealphadebuggers@gmail.com", Email_Password)
        SUBJECT = "Alpha Trip"
        TEXT = f"Hi {username}! We will look into your message and send you a reply as soon as possible if needed. Thank you for using Alpha Trip!"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        s.sendmail("thealphadebuggers@gmail.com", f"{email}", message)

        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("thealphadebuggers@gmail.com", Email_Password)
        SUBJECT = "Contact"
        TEXT = f"Using the email address {email}, here is a message from {username}: {msg}"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        s.sendmail("thealphadebuggers@gmail.com", "thealphadebuggers@gmail.com", message)

        s.quit()
        

      
        return redirect('/')
  else:
        return render(request,'contact.html')
        return redirect('contact')
 





    
