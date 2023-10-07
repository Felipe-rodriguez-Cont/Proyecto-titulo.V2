from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

#registrarse 
def index(request):
    if request.method == 'GET':
        print("enviando formulario")
        return render(request,'signup/signup.html',{                
        'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'])
                password=request.POST['password1']
                user.save()
                return HttpResponse ('usuario creado correctamente')
                
            except:
                return HttpResponse('usuario ya existe')
        return HttpResponse('contraseñas no coinciden')
    

#inicio sesion
def login(request):
    return render(request,'login/login.html')

def home(request):
    return render(request,'home/home.html')
