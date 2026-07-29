from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) 
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):

    
    id_user = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    photo_profil = models.URLField(max_length=500, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Requis pour l'admin Django

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'  # Identifiant principal
    REQUIRED_FIELDS = 'nom'  # Requis lors du createsuperuser

    def __str__(self):
        return self.email

    



class Categorie(models.Model):
    id_categorie = models.BigAutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.nom_categorie


class Don(models.Model):
    id_don = models.BigAutoField(primary_key=True)
    STATUT_CHOICES = [
        ("disponible", "Disponible"),
        ("reserve", "Réservé"),
        ("recupere", "Récupéré"),
    ]

    titre = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    quantite = models.PositiveIntegerField()
    photo_don = models.JSONField(max_length=500, blank=True, null=True)

  
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    date_publier = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="disponible")
    message = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dons')
    # PROTECT au lieu de CASCADE : empêche la suppression d'une catégorie
    # tant que des dons y sont rattachés.
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, related_name='dons')

    def __str__(self):
        return f"{self.user.username} - {self.statut} - {self.titre}"


class Reservation(models.Model):
    STATUT_CHOICES = [
        ("en_attente", "En attente"),
        ("confirme", "Confirmé"),
        ("recupere", "Récupéré"),
        ("annule", "Annulé"),  
    ]

    id_Reservation = models.BigAutoField(primary_key=True)

    date_reservation = models.DateTimeField(auto_now_add=True)
    # Renommé status -> statut pour rester cohérent avec les autres modèles
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="en_attente")
    message = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    don = models.ForeignKey(Don, on_delete=models.CASCADE, related_name='reservations')

    class Meta:
        constraints = [
            # Empêche deux réservations actives simultanées sur le même don
            models.UniqueConstraint(
                fields=['don'],
                condition=models.Q(statut__in=['en_attente', 'confirme']),
                name='une_seule_reservation_active_par_don',
            )
        ]

    def __str__(self):
        return f"Réservation par {self.user.username} pour {self.don.titre} ({self.statut})"


class Notification(models.Model):

    id_notification = models.BigAutoField(primary_key=True)
    STATUT_CHOICES = [("non_lu", "Non lu"), ("lu", "Lu")]

    message = models.TextField()
    date_notification = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="non_lu")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    def __str__(self):
        return f"{self.user.username} - {self.statut}"


class Signalisation(models.Model):
    STATUT_CHOICES = [("non_lu", "Non lu"), ("lu", "Lu")]
  

    id_signalisation = models.BigAutoField(primary_key=True)
    message = models.TextField()
    date_signalisation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default="non_lu")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='signalisations_faites')
    

    



    def __str__(self):
        cible = self.don_signale or self.utilisateur_signale
        return f"Signalement de {self.user.username} - {self.message} - {self.statut}"
