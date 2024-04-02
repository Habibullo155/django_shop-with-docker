from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'simple site with django',
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About us',
        'content': 'Welcome to about page'
    }
    return render(request, 'about.html', context)
