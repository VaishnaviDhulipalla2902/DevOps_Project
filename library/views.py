from django.shortcuts import render

from .models import Post
# from django.http import HttpResponse

def home(request):
    context={
        'posts' : Post.objects.all()
    }
    return render(request, 'library/home.html', context)


def about(request):
    return render(request, 'library/about.html')
