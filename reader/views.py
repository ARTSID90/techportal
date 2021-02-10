from django.shortcuts import render


def tech(request):
    return render(request, 'tech-index.html', {})


def single(request):
    return render(request, 'tech-single.html', {})


def article1(request):
    return render(request, '../templates/article/article 1.html', {})


def article2(request):
    return render(request, '../templates/article/article 2.html', {})