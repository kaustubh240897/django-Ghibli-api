from django.contrib.auth.models import User
from rest_framework.test import APIClient, force_authenticate
from rest_framework import status
from django.test import TestCase
from .models import Movie, Actor
from datetime import date

class MovieDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Log in the client
        self.client.force_authenticate(user=self.user)

        # Create some dummy data with a release_date
        self.actor = Actor.objects.create(id='1', name='Actor 1', species='Human', url='https://example.com/actor1')
        self.movie = Movie.objects.create(title='Movie 1', description='Description 1', release_date=date.today())
        self.movie.actors.add(self.actor)

    def test_movie_detail_view(self):
        url = f'/api/movies/{self.movie.pk}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data)
        self.assertIn('description', response.data)
        self.assertIn('actors', response.data)
        self.assertEqual(len(response.data['actors']), 1)
        self.assertEqual(response.data['actors'][0]['name'], 'Actor 1')

    def test_cached_movie_detail_view(self):
        url = f'/api/movies/{self.movie.pk}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data)
        self.assertIn('description', response.data)
        self.assertIn('actors', response.data)
        self.assertEqual(len(response.data['actors']), 1)
        self.assertEqual(response.data['actors'][0]['name'], 'Actor 1')

        # Fetch again to check if data is served from the cache
        response_cached = self.client.get(url)

        self.assertEqual(response_cached.status_code, status.HTTP_200_OK)
        self.assertEqual(response_cached.data, response.data)  # Ensure data is the same as the first request
