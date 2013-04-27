# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Post

def getRecentPosts(request):
    #Get all blog posts
    posts = Post.objects.all()

    #Sort posts
    sorted_posts = posts.order_by('-pub_date')

    #Display all posts
    return render_to_response('posts.html', { 'posts':sorted_posts})
