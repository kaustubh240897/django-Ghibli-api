from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timedelta

class MovieListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get(self, request, *args, **kwargs):
        # Check if the data is already in the cache
        cached_data = cache.get('movie_list')
        if cached_data:
            return Response(cached_data)

        # If not in cache or cache is expired, fetch fresh data
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)

        # Store the data in the cache with a 1-minute timeout
        cache.set('movie_list', serializer.data, 60)

        return Response(serializer.data)

class MovieDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer  # Define the serializer class here

    def get(self, request, *args, **kwargs):
        # Check if the data is already in the cache
        cached_data = cache.get(f'movie_details_{self.kwargs["pk"]}')
        if cached_data:
            return Response(cached_data)

        # If not in cache or cache is expired, fetch fresh data
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Store the data in the cache with a 1-minute timeout
        cache.set(f'movie_details_{self.kwargs["pk"]}', serializer.data, 60)

        return Response(serializer.data)
