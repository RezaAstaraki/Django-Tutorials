from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["profile_img"]

# print(Profile.profile_img)
