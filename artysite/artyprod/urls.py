from django.urls import path  #,include
from . import views
from django.contrib import admin
from .views import contact, contact_success
urlpatterns = [	
    path('', views.index,name='index'),

    path('register/', views.register, name='register'),

    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),

    path('equipes/',views.equipes, name = 'equipes'), 
    path('ajouter equipe/', views.ajouterEquipe, name='add_equipe'),
    path('<int:equipe_id>/edit_equipe/', views.edit_equipe, name='edit_equipe'),
    path('<int:equipe_id>/delete_equipe/', views.delete_equipe, name='delete_equipe'),
    path('<int:equipe_id>/detail_equipe', views.detail_equipe, name='detail_equipe'),

    path('personnel/', views.personnel, name='personnel'),
    path('TtPersonnel/', views.TtPersonnel, name='TtPersonnel'),
    path('deletePersonnel/<int:pk>/', views.delete_personnel, name='delete_personnel'),
    path('editPersonnem/<int:pk>/', views.edit_personnel, name='edit_personnel'),
    path('Personnel/<int:prs_id>/', views.detail_personnel, name='detail_personnel'),

    path('portfolio/', views.projetrea, name='projetrea'),
    path('createProjet/', views.create_projet, name='create_projet'),
    path('<int:proj_id>/detail_projet/', views.detail_projet, name='detail_projet'),
    path('<int:proj_id>/edit_projet/', views.edit_projet, name='edit_projet'),
    path('demande_prj/', views.create_demande, name='create_demande'),

    path('service/', views.service, name='service'),
    path('ajouter service/', views.add_service, name='add_service'),

    path('projets/', views.projetnr, name='projetnr'),
    path('createProjetnonrealise/', views.add_prjotnr, name='add_prjotnr'),

    path('Blog/', views.Blog, name='Blog'),


]