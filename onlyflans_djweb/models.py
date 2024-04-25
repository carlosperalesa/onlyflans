from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Product(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos", blank=True)
    slug = models.SlugField(unique=True)
    flan_uuid = models.UUIDField(default=uuid.uuid4)
    is_private = models.BooleanField(default=False)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(instance.nombre)
        unique_slug = slug
        num = 1
        while sender.objects.filter(slug=unique_slug).exists():
            num += 1
            unique_slug = '{}-{}'.format(slug, num)
        instance.slug = unique_slug


pre_save.connect(pre_save_receiver, sender=Product)
