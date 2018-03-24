from django import forms
from blog.models import Post,Comment
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text': forms.Textarea(attrs = {'class':'editable medium-editor-textarea'}),
        }

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'User Name'
        self.fields['email'].label = 'Email Address'
        