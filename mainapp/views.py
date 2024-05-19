from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from profileapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .helpers import send_forgetpass_mail
import uuid
from django.contrib import messages


# @login_required(login_url='login')
def homepage(request):
    books = Book.objects.order_by('-created_at')[:15]
    return render(request,'home.html',{'books':books,'room_name': "broadcast"})


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Invalid Username or Password !')
    return render(request, 'login.html')
 

def signuppage(request):
     if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        if password1!=password2:
            return HttpResponse('Invalid confirm password !')
        else:
            my_user=User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect('login')
        
     return render(request,'signup.html')
 
def logoutpage(request):
    logout(request)
    return redirect('home')

def delete_user(request,username):
    user=User.objects.get(username=username)
    
    if request.method=="POST":
        user.delete()
        messages.success(request,"account Deletion Successfull")
        return redirect('signup')
    
    return render(request,'users/delete_user.html')   
 


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=request.user.userprofile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to user profile page
#     else:
#         form = ProfileForm(instance=request.user.userprofile)
#     return render(request, 'profile/edit_profile.html', {'form': form})


    
   

