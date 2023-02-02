#Control de los templates y redirecionamiento
from django.shortcuts import render, redirect
#Mensajes de sesion rapida
from django.contrib import messages
#Control y creacion de los formularios de inicio de sesion
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
#Restringe el acceso al contenido si no estas logeado
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html',{
        'title': 'Inicio'
    })

def nosotros(request):
    return render(request, 'mainapp/nosotros.html',{
        'title': 'Sobre Nosotros'
    })

def register_page(request):

    register_form = RegisterForm()

    if request.user.is_authenticated:
        return redirect('inicio') 

    else:

        if request.method == 'POST':
            register_form=RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request,'Te has registrado exitosamente')

                #Utilizamos el name de la url
                return redirect('inicio')
        return render(request,'users/register.html',{
            'title':'Registro',
            'register_form': register_form,
    })

def login_page(request):

    if request.user.is_authenticated:
        return redirect('inicio') 

    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request,    username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('inicio')

            else:
                messages.warning(request,'No te has identificado correctamente')

        return render(request,'users/login.html',{
            "title":"Identificate",
    })

def logout_user(request):
    logout(request)
    return redirect('login')