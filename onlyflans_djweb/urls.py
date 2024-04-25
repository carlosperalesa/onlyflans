"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from onlyflans_djweb.views import index, footer, header, bienvenidos, productos, acerca, contacto


urlpatterns = [

    path('', index, name='index'),
    path('footer/', footer, name='footer'),
    path('header/', header, name='header'),
    path('bienvenidos/', bienvenidos, name='bienvenidos'),
    path('acerca/', acerca, name='acerca'),
    path('contacto/', contacto, name='contacto'),
    path('productos/', productos, name='productos'),

]

# handler404 = views.error_404
