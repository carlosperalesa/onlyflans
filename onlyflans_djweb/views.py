from onlyflans_djweb.models import Product
from django.shortcuts import render
from django.shortcuts import render, redirect
from onlyflans_djweb.forms import ContactForm, CustomUserCreationForm
from onlyflans_djweb.models import Product, User, Contact
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return render(request, 'index.html')


def footer(request):
    return render(request, 'footer.html')


def header(request):
    return render(request, 'header.html')


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
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, 'Tu registro se ha completado con éxito. ¡Bienvenido a la comunidad!')
            return redirect('login')
        else:
            messages.error(
                request, 'Hubo un problema con tu registro. Por favor, intenta de nuevo.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def salir(request):
    logout(request)
    return redirect('/')


@login_required
def tables(request):
    products = Product.objects.all()
    users = User.objects.all()
    contacto = Contact.objects.all()
    context = {
        'products': products,
        'users': users,
        'contacts': contacto,
    }

    return render(request, 'tables.html', context)
