from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    First_name=models.CharField(max_length=50,blank=True)
    Last_name=models.CharField(max_length=50, blank=True)
    bio=models.TextField(blank=True)
    profile_picture=models.ImageField(default='static/images/profile_pics/default.png' ,blank=True,null=True)
    location=models.CharField( max_length=50, blank=True)
    dob=models.DateField(blank=True, null=True)
    institution=models.CharField(max_length=100, blank=True)
    facebook=models.URLField(blank=True)
    instagram=models.URLField(blank=True)
    telegram=models.URLField(blank=True)
    
    
    def __str__(self):
        return self.user.username


class Book(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100,null=True)
    genre=models.CharField(max_length=100,null=True)
    availability = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class BookRequest(models.Model):
    sender = models.ForeignKey(User,related_name='sent_request', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name='received_request', on_delete=models.CASCADE,default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    schedule = models.DateTimeField()
    
# class Messages(models.Model):
#     sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
#     receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
    


    
    
