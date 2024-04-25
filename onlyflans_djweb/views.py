from django.shortcuts import render, redirect
from onlyflans_djweb.forms import ContactForm
from onlyflans_djweb.models import Product
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def footer(request):
    return render(request, 'footer.html')


def header(request):
    return render(request, 'header.html')


def bienvenidos(request):
    return render(request, 'bienvenidos.html')


def productos(request):
    producto = Product.objects.all()
    return render(request, 'productos.html', {"productos": producto})


def acerca(request):
    return render(request, 'acerca.html')


def contacto(request):
    if request.method == 'POST':
        contacto_form = ContactForm(request.POST)
        if contacto_form.is_valid():
            contacto_form.save()
            messages.success(
                request, 'Gracias por contactarnos, nos pondremos en contacto contigo en breve.')
            # Redirige a la misma página de contacto
            return redirect('contacto')
    else:
        contacto_form = ContactForm()

    return render(request, 'contacto.html', {"form": contacto_form})


# def error_404(request, exception):
#     return render(request, 'onlyflans_djweb\templates\custom\404.html')
