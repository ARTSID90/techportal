from django import forms


class ContactForm(forms.Form):
    #name = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Тема',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
