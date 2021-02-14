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
            mail = send_mail(form.cleaned_data['subject'],
                             form.cleaned_data['massage'],
                            'sitdikov365@gmail.com',
                             ['artem028_90@mail.ru'],
                             fail_silently=False)
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
    return render(request, 'tech-single.html', {})


def article1(request):
    return render(request, '../templates/article/article 1.html', {})


def article2(request):
    return render(request, '../templates/article/article 2.html', {})


def articlea51(request):
    return render(request, '../templates/article/article a51.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        # send an email
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Day: " + your_date + " Message: " + your_message

        send_mail(
            'Appointment Request',  # subject
            appointment,  # message
            your_email,  # from email
            ['sitdikov365@gmail.com'],  # To Email
        )

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'tech-index.html', {})