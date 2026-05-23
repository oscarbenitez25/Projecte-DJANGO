"""
Vistes del blog.

Aquest mòdul conté les funcions de vista per a l'aplicació blog.
Gestiona les pàgines d'inici, llistat de posts, detall de post,
autors i etiquetes.
"""

from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def starting_page(request):
    """
    Vista de la pàgina d'inici.
    Mostra els 3 posts més recents ordenats per data.
    """
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    """
    Vista del llistat de tots els posts.
    Mostra tots els posts ordenats per data descendent.
    """
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/post_list.html", {"posts": all_posts})


def post_detail(request, slug):
    """
    Vista del detall d'un post.
    Mostra el contingut complet d'un post identificat pel seu slug.
    Retorna 404 si el post no existeix.
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


def authors(request):
    """
    Vista del llistat de tots els autors.
    """
    all_authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {"authors": all_authors})


def author_detail(request, id):
    """
    Vista del detall d'un autor.
    Mostra la informació de l'autor i els seus posts.
    Retorna 404 si l'autor no existeix.
    """
    author = get_object_or_404(Author, id=id)
    return render(request, "blog/author_detail.html", {"author": author})


def tags(request):
    """
    Vista del llistat de totes les etiquetes.
    """
    all_tags = Tag.objects.all()
    return render(request, "blog/tags_list.html", {"tags": all_tags})


def tag_posts(request, id):
    """
    Vista dels posts d'una etiqueta.
    Mostra tots els posts que contenen una etiqueta específica.
    Retorna 404 si l'etiqueta no existeix.
    """
    tag = get_object_or_404(Tag, id=id)
    tag_posts = tag.posts.all().order_by("-date")
    return render(request, "blog/tag_posts.html", {"tag": tag, "posts": tag_posts})


def error_404(request, exception):
    """
    Vista de la pàgina d'error 404.
    """
    return render(request, "404.html", status=404)