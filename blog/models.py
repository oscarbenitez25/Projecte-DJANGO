"""
Models del blog.

Aquest mòdul defineix els models de base de dades per a l'aplicació blog:
Author, Tag i Post amb les seves relacions.
"""

from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    """
    Model que representa un autor del blog.
    Conté el nom, cognom i email de l'autor.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        """Retorna el nom complet de l'autor."""
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    """
    Model que representa una etiqueta del blog.
    El nom de l'etiqueta és únic.
    """
    caption = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """Retorna el nom de l'etiqueta."""
        return self.caption


class Post(models.Model):
    """
    Model que representa un post del blog.
    Conté el títol, excerpt, contingut, data, slug, autor i etiquetes.
    Relació One-to-Many amb Author i Many-to-Many amb Tag.
    """
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    excerpt = models.TextField(max_length=300)
    image_name = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        """Retorna el títol del post."""
        return self.title