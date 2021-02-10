from django.shortcuts import render


def tech(request):
    return render(request, 'tech-index.html', {})


def single(request):
    return render(request, 'tech-single.html', {})


def article1(request):
    return render(request, '../reader/templates/article/article 1.html', {})


def article2(request):
    return render(request, '../reader/templates/article/article 2.html', {})


def articlea51(request):
    return render(request, '../reader/templates/article/article a51.html', {})