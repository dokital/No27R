# Create your views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from blog.models import Post

def getPosts(request, selected_page=1):
    #Get all blog posts and sort
    posts = Post.objects.all().order_by('-pub_date')

    #Pages
    pages = Paginator(posts, 10)
    returned_page = pages.page(selected_page)

    #Display all posts
    return render_to_response('posts.html', {'posts':returned_page.object_list})
