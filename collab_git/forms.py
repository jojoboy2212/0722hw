from django import forms
from .models import Post, Review
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'publication_date' )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =('review', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password' : forms.PasswordInput()

            
        }