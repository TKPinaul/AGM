from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from .models import Utilisateur, RendezVous

class UtilisateurRegistrationForm(UserCreationForm):
    nom = forms.CharField(
        max_length=30, 
        required=True, 
        help_text='Required.')

    prenom = forms.CharField(
        max_length=30, 
        required=True, 
        help_text='Required.')

    email = forms.EmailField(
        max_length=254, 
        help_text='Required. Veuillez entrer une adresse mail Valide !!',
        widget=forms.TextInput(
            attrs={
                'placeholder':'exemple@gmail.co'})
        )

    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilisateur.objects.filter(email = email).exists():
            raise ValidationError("Ce compte est deja existant !!")
        return email

class UtilisateurLoginForm(forms.Form):
    username = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'autofocus': True}),
        label='Email',
        help_text='Required. Veuillez entrer une adresse mail Valide !!',
        error_messages={'invalid': 'Veuillez saisir un email valide !'}
    )
    password = forms.CharField(
        label="Password",
        help_text='Required. Veuillez verifier votre mots de passe !!',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            utilisateur = Utilisateur.objects.get(email=email)
            if not check_password(password, utilisateur.password):
                raise ValidationError("Le Mots de passe est incorrect")
        except Utilisateur.DoesNotExist:
            raise ValidationError("Le compte n'existe pas, veuillez vous enregistrer")

        return utilisateur

class RendezVousForm(forms.ModelForm):
    nom = forms.CharField(
        max_length=100, 
        required=True,
        )
    prenom = forms.CharField(
        max_length=100, 
        required=True, 
        )    
    adresse = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'exemple@gmail.co'
            }), 
        )    
    contact = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'00 00 00 00'
            }),
        )    
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'rows': 7,
                'cols': 50, 
                'placeholder':'Présenter une description de la cause de cette demande'
                }),
        )    
    nature_assistance = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'rows': 7,
                'cols': 50, 
                'placeholder':'Quel genre d\'assistance attendez vous de nous'
                }), 
        )
    
    class Meta:
        model = RendezVous
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(RendezVousForm, self).__init__(*args, **kwargs)
        
