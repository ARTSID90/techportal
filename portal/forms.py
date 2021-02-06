from django import forms


class ContactForm(forms.Form):
    #recipient_list = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #from_email = forms.EmailField(label='@', widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Ваше имя и Номер телефоа',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    massage = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
