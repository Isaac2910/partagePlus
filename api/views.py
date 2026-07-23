from django.shortcuts import render, get_object_or_404

from .models import User, Categorie, Don, Reservation, notification, Signalisation

from .serializers import UserSerializer, CategorieSerializer, DonSerializer, ReservationSerializer, notificationSerializer, SignalerSerializer        
from rest_framework import generics


from rest_framework.reverse import reverse

from django.http import JsonResponse, response, HttpResponse
from rest_framework import permissions


#root view for the API
class api_root(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'users': reverse('user-list-create', request=request),
            'categories': reverse('categorie-list-create', request=request),
            'donations': reverse('don-list-create', request=request),
            'reservations': reverse('reservation-list-create', request=request),
            'notifications': reverse('notification-list-create', request=request),
            'signalisations': reverse('signalisation-list-create', request=request),
        })
    
    def post(self, request, *args, **kwargs):
        return JsonResponse({
            'users': reverse('user-list-create', request=request),
            'categories': reverse('categorie-list-create', request=request),
            'donations': reverse('don-list-create', request=request),
            'reservations': reverse('reservation-list-create', request=request),
            'notifications': reverse('notification-list-create', request=request),
            'signalisations': reverse('signalisation-list-create', request=request),
        })
    
    def put(self, request, *args, **kwargs):
        return JsonResponse({
            'users': reverse('user-list-create', request=request),
            'categories': reverse('categorie-list-create', request=request),
            'donations': reverse('don-list-create', request=request),
            'reservations': reverse('reservation-list-create', request=request),
            'notifications': reverse('notification-list-create', request=request),
            'signalisations': reverse('signalisation-list-create', request=request),
        })
    
    def delete(self, request, *args, **kwargs):
        return JsonResponse({
            'users': reverse('user-list-create', request=request),
            'categories': reverse('categorie-list-create', request=request),
            'donations': reverse('don-list-create', request=request),
            'reservations': reverse('reservation-list-create', request=request),
            'notifications': reverse('notification-list-create', request=request),
            'signalisations': reverse('signalisation-list-create', request=request),
        })




#user views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id_user'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



#categorie views
class CategorieListCreateView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    lookup_field = 'id_categorie'



#don views
class DonListCreateView(generics.ListCreateAPIView):
    queryset = Don.objects.all()
    serializer_class = DonSerializer

class DonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Don.objects.all()
    serializer_class = DonSerializer
    lookup_field = 'id_don'


#reservation views
class ReservationListCreateView(generics.ListCreateAPIView):   
    
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id_reservation'


#notification views
class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = notification.objects.all()
    serializer_class = notificationSerializer


class NotificationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = notification.objects.all()
    serializer_class = notificationSerializer
    lookup_field = 'id_notification'

#signalisation views
class SignalisationListCreateView(generics.ListCreateAPIView):
    queryset = Signalisation.objects.all()
    serializer_class = SignalerSerializer


class SignalisationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Signalisation.objects.all()
    serializer_class = SignalerSerializer
    lookup_field = 'id_signalisation'

