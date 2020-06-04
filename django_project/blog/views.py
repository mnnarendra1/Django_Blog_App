from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def devops(request):
    return render(request, 'blog/devops.html')

def ai(request):
    return render(request, 'blog/ai.html')

# Create your post here.

posts = [
    {
        'title' : 'Blog Post 1: Amazon Cloud Products',
        'link' : 'https://aws.amazon.com/products/'
    },
    {
        'title' : 'Blog Post 2: Google Cloud Products',
        'link' : 'https://cloud.google.com/gcp/'
    },
    {
        'title' : 'Blog Post 3: Microsoft Cloud Products',
        'link' : 'https://azure.microsoft.com/en-us/services/'
    }

]

def business(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/business.html', context)

