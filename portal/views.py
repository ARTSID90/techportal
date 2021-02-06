from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm


def tech(request):
    return render(request, 'tech-index.html', {})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['massage'],
            'sitdikov365@gmail.com', ['artem028_90@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('tech-index')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'tech-contact.html', {"form": form})


def gadget(request):
    return render(request, 'gadget.html', {})


def video(request):
    return render(request, 'video.html', {})


def single(request):
    return render(request, 'tech-single.html')