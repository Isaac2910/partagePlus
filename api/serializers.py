from rest_framework import serializers

from rest_framework.renderers import JSONRenderer

from .models import User, Categorie, Don, Reservation , Notification , Signalisation

class UserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = ['id_user', 'nom', 'email', 'latitude', 'longitude', 'role_user']
        owner = serializers.ReadOnlyField(source="owner.username")


class CategorieSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Categorie
        fields = ['id_categorie', 'nom_categorie', 'description']

    


class DonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Don
        fields = ['id_don', 'titre', 'description', 'date_publier', 'date_expiration', 'categorie']
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id_reservation', 'id_user', 'id_don', 'date_reservation', 'statut_Reserv']  
        
 


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id_notification', 'user', 'message', 'date_notification', 'statut']
        read_only_fields = ['id_notification', 'date_notification']

      

class SignalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signalisation
        fields = ['id_signalisation', 'user', 'message', 'date_signalisation', 'statut']
        read_only_fields = ['id_signalisation', 'date_signalisation']