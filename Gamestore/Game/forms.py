from django import forms
from Game.models import Product #for class meta
# below desc - after creating form we have 2 optiion .form & ModelForm 1.form- if we use that we can only create from but if we used ModelForm - then its search for model like model.py and take from there its take Product
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productName','description','manufacturer','cat','price','image']  #thats data we going to take form owner 
        exclude =['is_available']

class UpdateProductForm(forms.ModelForm):
    class Meta:           #we used class Meta for decide which data need  to show which one is not that purpose  
        model = Product
        fields = ['image','productName','description','manufacturer','cat','price','is_available']  #thats data we going to take form owner 
        exclude =['']

class RegisterUserForm(forms.ModelForm):

    password= forms.CharField(max_length=10,widget=forms.PasswordInput)
    password2 =forms.CharField(max_length=10,widget=forms.PasswordInput)

    class Meta:                 
        model = User
        fields = ['username','first_name','last_name','email','password','password2']
        exclude =['last_login','is_superuser','is_staff','is_active','date_joined']

class LoginUserForm(forms.Form):    
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)