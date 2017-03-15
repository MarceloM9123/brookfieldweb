from django.shortcuts import render


def index(request):
    return render(request, 'burgerantics/index.html')


def two(request):
    return render (request, 'touche/two.html')
