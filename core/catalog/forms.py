from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import forms as auth_forms
from django.core.validators import RegexValidator
from django.db import models
user_model = get_user_model()

class RegisterForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

    class Meta:
        model = user_model
        fields = ('username', 'email', 'first_name', 
        
        #'last_name','middle_name', 'phone_number', 
        
        'password1', 'password2')



class UserEditForm(auth_forms.UserChangeForm):
    password = None
    class Meta:
        model = user_model
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name',
            'phone_number', 'gender', 'photo')