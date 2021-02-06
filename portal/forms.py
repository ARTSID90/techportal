from django import forms


class ContactForm(forms.Form):
    #name = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Номер телефона',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
