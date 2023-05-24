from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from . import views
from django.template import loader
from .forms import ContactForm,EquipeForm,PersonnelForm,ProjetForm,ServiceForm,ProjetnrForm,DemandeProjetForm
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.conf import settings

def index(request):
  return render(request,'artyprod/accueil.html' )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')  # Assuming 'accueil' is the URL name for the homepage
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
@login_required
def equipes(request):	
	Equipes= Equipe.objects.all()
	context={'Equipes':Equipes}
	return render(request,'artyprod/equipe/equipes.html',context )


"""def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'artyprod/contact.html', context)
"""

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']

        message_body = f"Name: {name}\nEmail : {email}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['artysitesoc4442@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'artyprod/contact.html', {'success': True})
    return render(request, 'artyprod/contact.html')


def contact_success(request):
    return render(request, 'artyprod/contact_success.html')


@permission_required('artyprod.Equipe.add_equipe.html')
def ajouterEquipe(request):
    if request.method == "POST" :
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save() 
            Equipes=Equipe.objects.all()
            return render(request,'artyprod/Equipe/equipes.html',{'equipes':equipes})
    else : 
            form = EquipeForm() #créer formulaire vide 
            Equipes=Equipe.objects.all()
            return render(request,'artyprod/Equipe/add_equipe.html',{'form':form,'equipes':equipes})

@permission_required('artyprod.Equipe.edit_equipe.html')
def edit_equipe(request,equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('equipes')
    else:
        form = EquipeForm(instance=equipe)
        return render(request, 'artyprod/Equipe/edit_equipe.html',{'form': form})

@permission_required('artyprod.Equipe.delete_equipe.html')
def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        equipe.delete()
        return redirect('equipes')
    return render(request, 'artyprod/equipe/delete_equipe.html', {'equipe': equipe})

@login_required
def detail_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    context = {'equipe': equipe}
    return render(request, 'artyprod/equipe/detail_equipe.html', context)


def TtPersonnel(request):
        personnels= Personnel.objects.all()
        context={'personnels':personnels}
        return render( request,'artyprod/personnels/personnels.html',context )

@permission_required('artyprod.personnels.create_prs.html')
def personnel(request):     
    if request.method == "POST":
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            personnels = Personnel.objects.all()
            return render(request, 'artyprod/personnels/personnels.html', {'personnels': personnels})
    else:
        form = PersonnelForm()
    personnels = Personnel.objects.all()
    return render(request, 'artyprod/personnels/create_prs.html', {'form': form, 'personnels': personnels})


@permission_required('artyprod.personnels.delete_prs.html')
def delete_personnel(request, pk):
    msg = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        msg.delete()
        return redirect('TtPersonnel')
    return render(request, 'artyprod/personnels/delete_prs.html', {'msg': msg})

@login_required
def detail_personnel(request, prs_id):
    personnel = get_object_or_404(Personnel, id=prs_id)
    context = {'personnel': personnel}
    return render(request, 'artyprod/personnels/detail_prs.html', context)



@permission_required('artyprod.personnels.edit_prs.html')
def edit_personnel(request, pk):
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('TtPersonnel')
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'artyprod/personnels/edit_prs.html', {'form': form})

@permission_required('artyprod.portfolio.create_projets.html')
def create_projet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            projets = ProjetRealise.objects.all()
            return render(request, 'artyprod/portfolio/projetrea.html', {'projets': projets})
    else:
        form = ProjetForm()
    projets = ProjetRealise.objects.all()
    return render(request, 'artyprod/portfolio/create_projets.html', {'form': form, 'projets': projets})


def projetrea(request):
    projets = ProjetRealise.objects.all()
    context = {'projets': projets}
    return render(request, 'artyprod/portfolio/projetrea.html', context)

@permission_required('artyprod.portfolio.create_projets.html')
def create_projet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetrea')
    else:
        form = ProjetForm()
    projets = ProjetRealise.objects.all()
    return render(request, 'artyprod/portfolio/create_projets.html', {'form': form, 'projets': projets})

@permission_required('artyprod.portfolio.edit_projets.html')
def edit_projet(request, proj_id):
    projet = get_object_or_404(ProjetRealise, id=proj_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projetrea')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'artyprod/portfolio/edit_projets.html', {'form': form})


def detail_projet(request, proj_id):
    projet = get_object_or_404(ProjetRealise, id=proj_id)
    context = {'projet': projet}
    return render(request, 'artyprod/portfolio/detail_projet.html', context)

def service(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'artyprod/services.html', context)


@permission_required('artyprod.add_service.html')
def add_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            services = Service.objects.all()
            return render(request, 'artyprod/services.html', {'projets': projets})
    else:
        form = ServiceForm()
    services = Service.objects.all()
    return render(request, 'artyprod/add_service.html', {'form': form, 'services': services})

@login_required
def projetnr(request):
    projetnrs = Projet.objects.all()
    context = {'projetnrs': projetnrs}
    return render(request, 'artyprod/projets/projetsnr.html', context)

@permission_required('artyprod.add_prj.html.html')
def add_prjotnr(request):
    if request.method == "POST":
        form = ProjetnrForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            projetnrs = Projet.objects.all()
            return render(request, 'artyprod/projets/projetsnr.html', {'projetnrs': projetnrs})
    else:
        form = ProjetnrForm()
    
    projetnrs = Projet.objects.all()
    return render(request, 'artyprod/projets/add_prj.html', {'form': form, 'projetnrs': projetnrs})


@login_required
def create_demande(request):
    if request.method == "POST":
        form = DemandeProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            prjs = DemandeProjet.objects.all()
            return render(request, 'artyprod/portfolio/succes.html', {'prjs': prjs})
    else:
        form = DemandeProjetForm()
    prjs = DemandeProjet.objects.all()
    return render(request, 'artyprod/portfolio/demande_projets.html', {'form': form, 'prjs': prjs})

def Blog(request):
   return render(request,'artyprod/Blog.html' )

