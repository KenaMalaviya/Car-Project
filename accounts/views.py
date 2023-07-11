from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.



def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                print('Username taken'),
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                print('Email taken')
                return redirect('/accounts/register')
            else:

                s = User.objects.create_user(first_name=fname,last_name = lname,username= uname,email=email,password=pass1)
                s.save()
                messages.success(request, "Your message has been successfully sent")
                print('Registration Successfully...')
                return redirect('/')
    
        else:
            print('Password not match')
            return redirect('/accounts/register')

    return render(request,'register.html')

def handlelogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=uname, password=pass1)
        if user is not None:
            auth.login(request,user)
            print('Login Successfully...')
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        
        else:
            print('invalid login details')
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/accounts/login')

    return render(request, 'login.html')

def handlelogout(request):
    auth.logout(request)
    print('Logout Successfully...')
    messages.success(request, "Your message has been successfully sent")
    return redirect('/')

def forgot(request):
    return render(request, 'forgot.html')

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('accounts:handlelogin')
