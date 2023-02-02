from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="Nombre Categoría")
    description= models.CharField(max_length=255, verbose_name="Descripción categoría")
    create_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el")

    class Meta:
        verbose_name: "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Article(models.Model):
    title= models.CharField(max_length=150,verbose_name="Titulo articulo")
    content= RichTextField(verbose_name="Contenido")
    imagen = models.ImageField(default='null', verbose_name="Imagen articulo",upload_to="articulos")
    public= models.BooleanField(verbose_name="Publicado?")
    create_at= models.DateTimeField(auto_now_add=True,verbose_name="Creado el")
    update_at= models.DateTimeField(auto_now=True,verbose_name="Editado el")
    user= models.ForeignKey(User,editable=False, verbose_name="Usuario", on_delete=models.CASCADE) #Objeto usuario que creo el articulo
    categories= models.ManyToManyField(Category, verbose_name="Categorías", blank=True, related_name="articles")

    class Meta:
        verbose_name: "Articulo"
        verbose_name_plural = "Articulos"
        ordering =  ['-create_at']

    def __str__(self):
        return self.title