from django.shortcuts import render

def home(request):
    context = {'val': "Menu Acceuil"}
    return render(request, 'home.html', context)