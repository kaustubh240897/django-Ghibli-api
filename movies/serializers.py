from rest_framework import serializers
from .models import Actor, Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'species', 'url']

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'actors']
