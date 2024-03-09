from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages

from apliGestMedical.models import Utilisateur, RendezVous
from .forms import UtilisateurRegistrationForm, UtilisateurLoginForm, RendezVousForm

# Fonction de base
def register(request):
    if request.method == 'POST':
        form = UtilisateurRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UtilisateurRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UtilisateurLoginForm(request.POST)
        if form.is_valid():
            try:
                email = request.POST.get('username')
                password = request.POST.get('password')

                utilisateur = Utilisateur.objects.get(email=email)
                if not check_password(password, utilisateur.password):
                    raise ValidationError("Le mot de passe est incorrect.")
                
                login(request, utilisateur)
                messages.success(request, 'Connexion réussie!')
                return redirect('accueil', user_id=utilisateur.id)
            
            except ValidationError as e:
                messages.error(request, request, str(e))
                print(f"Validation error: {str(e)}")
                
    else:
        form = UtilisateurLoginForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

#  page d'accueil (premiere page qui succede le login)
def accueil(request, user_id):
    users = Utilisateur.objects.get(id=user_id)
    return render(request, 'accueil.html', {'user_id': user_id})

def myUserCompte(request, user_id):
    users = Utilisateur.objects.get(id=user_id)
    return render(request, 'userCompte.html', {"user":users})

# page de rendez-vous (l'utilisateur fais une demande de rendez-vous)
def rendezVous(request, user_id):
    users = Utilisateur.objects.get(id=user_id)
    if request.method == 'POST':
        form = RendezVousForm(request.POST, request.FILES)
        if form.is_valid():
            rendezvous = form.save()
            # Faire ce que tu veux après la sauvegarde du rendez-vous
            return redirect('accueil')
    else:
        form = RendezVousForm()

    return render(request, 'fonctionnaliter/rendez_vous.html', {'form': form, 'user_id': user_id})

