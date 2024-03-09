from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, nom, prenom, password=None):
        if not email:
            raise ValueError('L\'adresse email est obligatoire.')

        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, prenom=prenom)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nom, prenom, password=None):
        user = self.create_user(email, nom, prenom, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Utilisateur(AbstractBaseUser):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

class RendezVous(models.Model):
    HOSPITAL_CHOICES = [
        ('Hopital1', 'Hôpital 1'),
        ('Hopital2', 'Hôpital 2'),
    ]

    PROFESSION_CHOICES = [
        ('Medecin', 'Médecin'),
        ('Ingenieur', 'Ingénieur'),
        ('Informaticien', 'Informaticien'),
        ('Secretair', 'Secrétair'),
        ('Agriculteu', 'Agriculteur'),
        ('Artisant', 'Artisant'),
        ('Professeur', 'Professeur'),
        ('Entrepreneur', 'Entrepreneur'),
    ]

    TYPE_PERSONNE_A_CONSULTER = [
        ('Nourrisson', 'Nourrisson'),
        ('Enfant', 'Enfant'),
        ('Adolescent', 'Adolescent'),
        ('Adulte', 'Adulte'),
        ('Personne agee', 'Personne âgée'),
        ('Femme enceinte', 'Femme enceinte'),
    ]

    SEXE_CHOICES = [
        ('Masculin', 'Masculin'),
        ('Feminin', 'Féminin'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Celibataire', 'Célibataire'),
        ('Couple', 'Couple'),
    ]

    date_demande = models.DateTimeField(auto_now_add=True)
    hospital = models.CharField(max_length=100, choices=HOSPITAL_CHOICES)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=50, choices=SEXE_CHOICES)
    age = models.PositiveIntegerField()
    situation_Matrimoniale = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES)
    profession = models.CharField(max_length=100, choices=PROFESSION_CHOICES, default='Autre')
    adresse = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    type_personne = models.CharField(max_length=50, choices=TYPE_PERSONNE_A_CONSULTER)
    description = models.TextField()
    nature_assistance = models.TextField()

    def __str__(self):
        return f"Rendez-vous pour {self.nom} {self.prenom} le {self.date.strftime('%d/%m/%Y')} à {self.hospital}"
    
class DocumentJustificatif(models.Model):
    rendezvous = models.ForeignKey(RendezVous, on_delete=models.CASCADE, related_name='documents')
    fichier = models.FileField(upload_to='documents_justificatifs/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Document pour {self.rendezvous.nom} {self.rendezvous.prenom} - {self.description[:50]}"