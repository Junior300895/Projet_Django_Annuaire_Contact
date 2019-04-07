from django import forms

class ContactForm(forms.Form):
    prenom = forms.CharField(label='Prénom', max_length=30)
    nom = forms.CharField(label='Nom', max_length=30)
    numero = forms.CharField(label='Numéro', max_length=10)
    email = forms.EmailField(label='Email', max_length=20)
    adresse = forms.CharField(label='Adresse', max_length=20)
    # image = forms.ImageField(label='Adresse')