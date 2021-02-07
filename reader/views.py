from django.shortcuts import render


def tech(request):
    return render(request, 'tech-index.html', {})


def single(request):
    return render(request, 'tech-single.html', {})


def article(request):
    return render(request, '../templates/article/article1.html', {})