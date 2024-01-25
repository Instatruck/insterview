from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer
from .crud.model_services import (get_all_actors, get_all_directors, get_all_movies)
from .models import Actor, Movie, Director
from django.shortcuts import get_object_or_404


class ActorListView(APIView):
    @extend_schema(summary="List all actors")
    def get(self, request):
        actors = get_all_actors()
        serializer = ActorSerializer(actors, many=True, context={'request': request})
        return Response(serializer.data)

class DirectorListView(APIView):
    @extend_schema(summary="List all directors")
    def get(self, request):
        directors = get_all_directors()
        serializer = DirectorSerializer(directors, many=True, context={'request': request})
        return Response(serializer.data)


class MovieListView(APIView):
    @extend_schema(summary="List all movies")
    def get(self, request):
        movies = get_all_movies()
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)
    
class ActorFilmsView(APIView):
    def get(self, request, name):
        actor = get_object_or_404(Actor, name=name)
        # Assuming a ForeignKey from Movie to Actor, you can directly access related movies
        movies = Movie.objects.filter(actor=actor)
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)
    
class DirectorFilmsView(APIView):
    def get(self, request, name):
        director = get_object_or_404(Director, name=name)
        movies = Movie.objects.filter(director=director)
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)