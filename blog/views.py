from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/post_list.html", {"posts": all_posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})

def authors(request):
    all_authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {"authors": all_authors})

def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, "blog/author_detail.html", {"author": author})

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, "blog/tags_list.html", {"tags": all_tags})

def tag_posts(request, id):
    tag = get_object_or_404(Tag, id=id)
    tag_posts = tag.posts.all().order_by("-date")
    return render(request, "blog/tag_posts.html", {"tag": tag, "posts": tag_posts})

def error_404(request, exception):
    return render(request, "404.html", status=404)