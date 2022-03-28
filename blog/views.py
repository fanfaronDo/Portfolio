from django.shortcuts import render, get_object_or_404
from .models import Blogs


def all_blogs(requests):
    blogs = Blogs.objects.all()[:5]
    return render(requests, 'blog/all_blogs.html', { 'blogs': blogs })


def detail(requests, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(requests, 'blog/detail.html', { 'blog': blog })


