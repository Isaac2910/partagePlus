
from django.urls import path
from .views import api_root, UserListCreateView, CategorieListCreateView, DonListCreateView, ReservationListCreateView, UserRetrieveUpdateDestroyView, CategorieRetrieveUpdateDestroyView, DonRetrieveUpdateDestroyView, ReservationRetrieveUpdateDestroyView, NotificationListCreateView, NotificationRetrieveUpdateDestroyView, SignalisationListCreateView, SignalisationRetrieveUpdateDestroyView


from rest_framework.urlpatterns import format_suffix_patterns





urlpatterns = [

    path("", api_root.as_view(), name="api-root"),

    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:id_user>/", UserRetrieveUpdateDestroyView.as_view(), name="user-retrieve-update-destroy"),

    path("categories/", CategorieListCreateView.as_view(), name="categorie-list-create"),
    path("categories/<int:id_categorie>/", CategorieRetrieveUpdateDestroyView.as_view(), name="categorie-retrieve-update-destroy"),

    path("don/", DonListCreateView.as_view(), name="don-list-create"),
    path("don/<int:id_don>/", DonRetrieveUpdateDestroyView.as_view(), name="don-retrieve-update-destroy"),

    path("reservations/", ReservationListCreateView.as_view(), name="reservation-list-create"),
    path("reservations/<int:id_reservation>/", ReservationRetrieveUpdateDestroyView.as_view(), name="reservation-retrieve-update-destroy"),

    path("notifications/", NotificationListCreateView.as_view(), name="notification-list-create"),
    path("notifications/<int:id_notification>/", NotificationRetrieveUpdateDestroyView.as_view(), name="notification-retrieve-update-destroy"),

    path("signalisations/", SignalisationListCreateView.as_view(), name="signalisation-list-create"),
    path("signalisations/<int:id_signalisation>/", SignalisationRetrieveUpdateDestroyView.as_view(), name="signalisation-retrieve-update-destroy"),

]

