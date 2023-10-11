from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login

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
    return render(request, 'login/login.html')

def home(request):
    return render(request, 'home/home.html')

def task(request):
    return render(request, 'tasks/tasks.html')

