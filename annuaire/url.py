from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.listercontact, name='contacts'),
    path('formulaire', views.get_contact_form, name='formulaire'),
    path('<int:contact_id>/', views.get_contacts_details, name='contacts_details'),
]