from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from annuaire.forms import ContactForm
from annuaire.models import Contact


def index(request):
    return HttpResponse("Salut le monde, vous êtes à la page annuaire")

def listercontact(request):
    list_contacts = Contact.objects.all()
    context = {'list_contacts': list_contacts}
    return render(request, 'annuaire/contacts.html', context)

def get_contact_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            contact = form.cleaned_data
            p = contact['prenom']
            n = contact['nom']
            num = contact['numero']
            email = contact['email']
            add = contact['adresse']
            c = Contact(prenom=p,nom=n,numero=num,email=email, adresse=add)
            c.save()
            # redirect to a new URL:
            return HttpResponseRedirect('contacts')
            # listercontact(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'annuaire/formulaire.html', {'form': form})
