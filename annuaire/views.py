from django.shortcuts import render
from django.http import HttpResponse

from annuaire.models import Contact


def index(request):
    return HttpResponse("Salut le monde, vous êtes à la page annuaire")

def listercontact(request):
    list_contacts = Contact.objects.all()
    context = {'list_contacts': list_contacts}
    return render(request, 'annuaire/contacts.html', context)
