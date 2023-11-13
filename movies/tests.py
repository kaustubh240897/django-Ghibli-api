from django.test import TestCase
from rest_framework.test import APIClient

class MovieApiTests(TestCase):
    def test_movie_list_view(self):
        client = APIClient()
        response = client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
