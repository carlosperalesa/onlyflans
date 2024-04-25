from django.shortcuts import render, redirect
from onlyflans_djweb.forms import ContactForm, CustomUserCreationForm
from onlyflans_djweb.models import Product
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def footer(request):
    return render(request, 'footer.html')


def header(request):
    return render(request, 'header.html')


@login_required
def productos(request):
    producto = Product.objects.all()
    return render(request, 'productos.html', {"productos": producto})


def acerca(request):
    return render(request, 'acerca.html')


def contacto(request):
    form_submitted = False
    contacto_form = ContactForm()
    if request.method == 'POST':
        contacto_form = ContactForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            form_submitted = True

    return render(request, 'contacto.html', {"form": contacto_form, "form_submitted": form_submitted})


def login(request):
    form = AuthenticationForm()  # Crea una instancia del formulario
    # Pasa el formulario al contexto
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Tu registro se ha completado con éxito. ¡Bienvenido a la comunidad!')
            return redirect('index')  # Redirige a la URL con nombre 'index'
        else:
            messages.error(
                request, 'Hubo un problema con tu registro. Por favor, intenta de nuevo.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def salir(request):
    logout(request)
    return redirect('/')
