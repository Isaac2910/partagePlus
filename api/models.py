from django.db import models
#from django.contrib.auth.models import AbstractBaseUser 


class User(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    photo_profil = models.JSONField()
    ville = models.CharField()

    est_actif = models.BooleanField()


    date_inscription = models.DateTimeField(auto_now_add=True)

    dernierre_connection = models.DateTimeField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)



    def __str__(self):
        return self.username
    
#
class Categorie(models.Model):
    id_categorie = models.BigAutoField(primary_key=True)
    nom_categorie = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200)

    def  __str__(self):
        return self.nom_categorie
    


    

class Don(models.Model):
    id_don = models.BigAutoField(primary_key=True)

    titre = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    type_don = models.CharField(max_length=50, choices=[("argent", "Argent"), ("nourriture", "Nourriture"), ("vetements", "Vêtements")])
    quantite = models.PositiveIntegerField()

    photo_don = models.JSONField(blank=True, null=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    address = models.CharField(max_length=255, null=True, blank=True)

    date_publier = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField(null=True, blank=True)

    statut = models.CharField(max_length=20, choices=[("disponible", "Disponible"), ("reserver", "Réservé")], default="disponible")

    message = models.TextField()

    #clef e user Don
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='dons')
    #clef e don C
    id_categorie = models.ForeignKey( Categorie, on_delete=models.CASCADE)

    

    def __str__(self):
        return f"{self.id_user.username} - {self.statut} - {self.titre}"
    


class Reservation(models.Model):
    id_reservation = models.BigAutoField(primary_key=True)
    date_reservation = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=[("en_attente", "En attente"), ("confirmer", "Confirmer"), ("recuperer", "Recuperer")], default="en_attente")
    message = models.TextField()

    #clef e User_Reserv
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='reservations')
    
    

    def __str__(self):
        return f"{self.id_user.username} - {self.status} - {self.date_reservation}"
    