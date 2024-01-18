from django import forms
from .models import UserProfile
from .models import Book
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['First_name', 'Last_name', 'bio', 'profile_picture', 'location', 'dob','institution','facebook', 'instagram', 'telegram']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','genre','availability']


        