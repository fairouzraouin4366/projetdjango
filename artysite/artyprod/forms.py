from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm 
from .models import Equipe,Contact,Personnel,ProjetRealise,Service,Projet,DemandeProjet
from django import forms

class UserRegistrationForm(UserCreationForm):
      first_name = forms.CharField(label='Prénom')
      last_name = forms.CharField(label='Nom')
      email = forms.EmailField(label='Adresse e-mail')
      class Meta(UserCreationForm.Meta):
         model = User
         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
class EquipeForm(ModelForm):
     class Meta : 
        model = Equipe
        fields = "__all__" #pour tous les champs de la table
        #fields=['libellé','description']  #pour qulques champs
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
class PersonnelForm(ModelForm):
     class Meta : 
        model = Personnel
        fields = "__all__" #pour tous les champs de la table
class ProjetForm(ModelForm):
     class Meta : 
        model = ProjetRealise
        fields = "__all__" #pour tous les champs de la table
class ServiceForm(ModelForm):
     class Meta : 
        model = Service
        fields = "__all__" #pour tous les champs de la table
class ProjetnrForm(ModelForm):
     class Meta : 
        model = Projet
        fields = "__all__" #pour tous les champs de la table
class DemandeProjetForm(ModelForm):
     class Meta : 
        model = DemandeProjet
        fields = "__all__" #pour tous les champs de la table
        #fields=['libellé','description']  #pour qulques champs