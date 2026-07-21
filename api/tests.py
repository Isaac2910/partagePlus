from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()

class APITestCase(TestCase):
    def test_api_root(self):
        url = reverse('api-root')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.json())
        self.assertIn('categories', response.json())
        self.assertIn('donations', response.json())
        self.assertIn('reservations', response.json())
        self.assertIn('notifications', response.json())
        self.assertIn('signalisations', response.json())

class UserAPITestCase(TestCase):
    def test_user_list_create(self):
        url = reverse('user-list-create')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_user_retrieve_update_destroy(self):
        # Create a user first
        user_data = {
            "username": "testuser",
            "email": "testuser@example.com"
        }
        response = client.post(reverse('user-list-create'), data=user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_id = response.json()['id']

        # Retrieve the user
        url = reverse('user-retrieve-update-destroy', kwargs={'pk': user_id})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the user
        update_data = {
            "username": "updateduser",
            "email": "updateduser@example.com"
        }
        response = client.put(url, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete the user
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  

class CategorieAPITestCase(TestCase):
    def test_categorie_list_create(self):
        url = reverse('categorie-list-create')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_categorie_retrieve_update_destroy(self):
        # Create a categorie first
        categorie_data = {
            "nom_categorie": "testcategorie",
            "description": "test description"
        }
        response = client.post(reverse('categorie-list-create'), data=categorie_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        categorie_id = response.json()['id']

        # Retrieve the categorie
        url = reverse('categorie-retrieve-update-destroy', kwargs={'pk': categorie_id})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the categorie
        update_data = {
            "nom_categorie": "updatedcategorie",
            "description": "updated description"
        }
        response = client.put(url, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete the categorie
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    class DonAPITestCase(TestCase):
        def test_don_list_create(self):
            url = reverse('don-list-create')
            response = client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsInstance(response.json(), list)

        def test_don_retrieve_update_destroy(self):
            # Create a don first
            don_data = {
                "titre": "testdon",
                "description": "test description",
                "type_don": "argent",
                "quantite": 10,
                "message": "test message",
                "id_user": 1,  # Assuming a user with id 1 exists
                "id_categorie": 1  # Assuming a categorie with id 1 exists
            }
            response = client.post(reverse('don-list-create'), data=don_data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            don_id = response.json()['id']

            # Retrieve the don
            url = reverse('don-retrieve-update-destroy', kwargs={'pk': don_id})
            response = client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # Update the don
            update_data = {
                "titre": "updateddon",
                "description": "updated description",
                "type_don": "nourriture",
                "quantite": 20,
                "message": "updated message",
                "id_user": 1,
                "id_categorie": 1
            }
            response = client.put(url, data=update_data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # Delete the don
            response = client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReservationAPITestCase(TestCase):
    def test_reservation_list_create(self):
        url = reverse('reservation-list-create')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_reservation_retrieve_update_destroy(self):
        # Create a reservation first
        reservation_data = {
            "id_user": 1,  # Assuming a user with id 1 exists
            "id_don": 1,  # Assuming a don with id 1 exists
        }
        response = client.post(reverse('reservation-list-create'), data=reservation_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        reservation_id = response.json()['id']

        # Retrieve the reservation
        url = reverse('reservation-retrieve-update-destroy', kwargs={'pk': reservation_id})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the reservation
        update_data = {
            "id_user": 1,
            "id_don": 1,
            "status": "confirmer"
        }
        response = client.put(url, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete the reservation
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class NotificationAPITestCase(TestCase):
    def test_notification_list_create(self):
        url = reverse('notification-list-create')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_notification_retrieve_update_destroy(self):
        # Create a notification first
        notification_data = {
            "id_user": 1,  # Assuming a user with id 1 exists
            "message": "test notification"
        }
        response = client.post(reverse('notification-list-create'), data=notification_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        notification_id = response.json()['id']

        # Retrieve the notification
        url = reverse('notification-retrieve-update-destroy', kwargs={'pk': notification_id})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the notification
        update_data = {
            "id_user": 1,
            "message": "updated notification"
        }
        response = client.put(url, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete the notification
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SignalisationAPITestCase(TestCase):
    def test_signalisation_list_create(self):
        url = reverse('signalisation-list-create')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_signalisation_retrieve_update_destroy(self):
        # Create a signalisation first
        signalisation_data = {
            "id_user": 1,  # Assuming a user with id 1 exists
            "message": "test signalisation"
        }
        response = client.post(reverse('signalisation-list-create'), data=signalisation_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        signalisation_id = response.json()['id']

        # Retrieve the signalisation
        url = reverse('signalisation-retrieve-update-destroy', kwargs={'pk': signalisation_id})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the signalisation
        update_data = {
            "id_user": 1,
            "message": "updated signalisation"
        }
        response = client.put(url, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete the signalisation
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

