from django import forms


class ContactForm(forms.Form):
    #name = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #from_email = forms.EmailField(label='@', widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Ваше имя и Номер телефоа',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    massage = forms.CharField(label='Текст', max_length=5000, widget=forms.Textarea({'class': 'form-control', "rows": 5}))