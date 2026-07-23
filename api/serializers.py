from rest_framework import serializers

from rest_framework.renderers import JSONRenderer

from .models import User, Categorie, Don, Reservation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'username', 'email', 'latitude', 'longitude', 'owner']
        owner = serializers.ReadOnlyField(source="owner.username")


class CategorieSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Categorie
        fields = ['id_categorie', 'nom_categorie', 'description']

    


class DonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Don
        fields = ['id_don', 'titre', 'description', 'date_publier', 'date_expiration', 'id_categorie']
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id_reservation', 'id_user', 'id_don', 'date_reservation']  
        
 


class notificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id_reservation', 'id_user', 'date_reservation','message'] 
        

class SignalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Don
        fields = ['id_don', 'titre', 'description', 'type_don', 'quantite', 'photo_don', 'latitude', 'longitude', 'address', 'date_publier', 'date_expiration', 'statut', 'message', 'id_user', 'id_categorie']