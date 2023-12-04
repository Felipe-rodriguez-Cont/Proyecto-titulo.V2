from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm

# registrarse
def index(request):
    if request.method == 'GET':
        print("enviando formulario")
        return render(request, 'signup/signup.html', {
            'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password = request.POST['password1'])
                user.save()
                login(request, user)
                print('pasa por login')
                return redirect('task')                
            except:
                return render(request, 'signup/signup.html', {
                    'form': UserCreationForm(),
                    'error':('usuario ya existe')
                    })
       
        return render(request, 'signup/signup.html', {
                    'form': UserCreationForm(),
                    'error':('Contraseñas no coinciden')
                    })
# inicio sesion
def sigin(request):
    if request.method == "GET":
        return render(request, 'login/login.html',{'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],password = request.POST['password'])
        if user is None:  
            return render(request, 'login/login.html',{
                    'form': AuthenticationForm,
                    'error':'usuario o contraseña incorrecto'
                    })
        else:
            login(request, user)
            return redirect('task')
  
def home(request):
    return render(request, 'home/home.html')

def task(request):
    return render(request, 'tasks/tasks.html')

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task/create_task.html',{
        'form': TaskForm
        })
    else:
        form =  TaskForm(request.POST)
        return render(request, 'create_task/create_task.html',{
        'form': TaskForm
        })   
    

def signout(request):
    logout (request) 
    return redirect('home')