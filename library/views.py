from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

posts = [
    {
        'author':'Vaishnavi Dhulipalla',
        'title' : 'Current Reads',
        'content': 'I am currently reading The Fountain Head by Ayn Rand.',
        'date_posted': 'May 1, 2021'
    },
        {
        'author':'Simran Basu',
        'title' : 'My all-time favourite book!',
        'content': '**Fill in some info**',
        'date_posted': 'May 1, 2021'
    }
]
def home(request):
    context={
        'posts' : Post.objects.all()
    }
    return render(request, 'library/home.html', context)


def about(request):
    return render(request, 'library/about.html')
