from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import UserProfileForm,BookForm
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages



def profile(request,username):
    if request.user.is_authenticated:
        Username=username
        user_profile = UserProfile.objects.get(user__username=username)
        users=User.objects.all()
        return render(request, 'profile/profile.html', {'Username':Username,'users':users,'user_profile': user_profile} )
    else:
        messages.success(request,"sign-up required !")
        return redirect('home')

def readers(request,username):
    users_profile= UserProfile.objects.all()
    user = User.objects.all()
    Username=username
    return render(request, 'reders/readers.html', {'Username':Username, 'user': user,'users_profile':users_profile})

@login_required
def EditProfile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'profile/edit_profile.html', {'form': form})



def about(request):
    return render(request, 'users/about.html')


def booklist(request,username):
    Username=username
    user2=User.objects.get(username=Username)
    user_booklist= Book.objects.all()
    return render(request, 'profile/booklist.html', {'user2':user2,'user_booklist': user_booklist})

def add_book(request):
   
    if request.method =="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        genre=request.POST.get('genre')
        availability=request.POST.get('availability',True)
        Book.objects.create(owner=request.user,title=title,author=author,genre=genre,availability=availability)
        messages.success(request,"Added Successfully")
        return redirect('add_book')
    
    return render(request,'profile/add_book.html')

def update_book(request,id):
    book= Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('update_book' ,id=id)
    else:
       form = BookForm(instance=book)
       
    return render(request,'profile/update_book.html',{'form': form})

def delete_book(request,id):
    book=Book.objects.get(id=id)
    
    if request.method=="POST":
        book.delete()
        messages.success(request, "Book deleted successfully")
        return redirect('booklist',username=request.user.username)
    
    return render(request, 'profile/delete_book.html',{'book':book})

def books(request):
    books= Book.objects.all()
    
    # search method begin
    if request.method=="POST":
        title=request.POST.get('title', '')
        book=Book.objects.filter( title=title)
        return render(request,'profile/book_search_result.html',{'book':book})
    
    # serach method end
    
    return render(request,'profile/books.html',{'books':books})


@login_required
def book_request(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        schedule=request.POST.get('schedule')
        book.availability=1
        book.save()
        BookRequest.objects.create(sender=request.user,receiver=book.owner,schedule=schedule, book=book)
        return redirect('home')

    return render(request, 'users/book_request.html', {'book': book})

@login_required
def see_book_request(request):
    requests = BookRequest.objects.filter(receiver=request.user)
    return render(request, 'users/see_book_request.html', {'requests': requests})

def confirm_request(request,book_id):
    book=Book.objects.get(pk=book_id)
    book.availability=2
    book.save()
    return redirect('see_book_request')
    
def reject_request(request,book_id):
    book=Book.objects.get(pk=book_id)
    request=BookRequest.objects.get(book=book)
    request.delete()
    book.availability=0
    book.save()
    return redirect('see_book_request')

@login_required
def borrowing_history(request):
    borrows = BookRequest.objects.filter(sender=request.user)
    return render(request, 'users/borrowing_history.html', {'borrows': borrows})
    
    

