from django.shortcuts import render


def tech(request):
    return render(request, 'tech-index.html', {})
