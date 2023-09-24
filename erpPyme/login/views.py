from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request,'signup/signup.html',{
        'form':UserCreationForm()})
    

#inicio sesion
def login(request):
    return render(request,'login/login.html')