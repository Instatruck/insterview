from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer, BestMovieSerializer
from .crud.model_services import (get_all_actors, get_all_directors, get_all_movies)
from .models import Actor, Movie, Director
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta

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
        start_year = request.query_params.get('start_year')
        end_year = request.query_params.get('end_year')

        # Validation for start_year and end_year
        if start_year:
            try:
                start_year = int(start_year)
            except ValueError:
                return Response({"error": "Invalid start year."}, status=status.HTTP_400_BAD_REQUEST)

        if end_year:
            try:
                end_year = int(end_year)
            except ValueError:
                return Response({"error": "Invalid end year."}, status=status.HTTP_400_BAD_REQUEST)

        if start_year and end_year and start_year > end_year:
            return Response({"error": "Start year cannot be greater than end year."}, status=status.HTTP_400_BAD_REQUEST)

        movies = get_all_movies()

        if start_year is not None:
            movies = movies.filter(year__gte=start_year)
        if end_year is not None:
            movies = movies.filter(year__lte=end_year)

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    
class ActorFilmsView(APIView):
    def get(self, request, id):
        actor = get_object_or_404(Actor, pk=id)
        films = actor.movie_set.all()
        serializer = MovieSerializer(films, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class DirectorFilmsView(APIView):
    def get(self, request, id):
        director = get_object_or_404(Actor, pk=id)
        films = director.movie_set.all()
        serializer = MovieSerializer(films, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TopRatedMoviesView(APIView):
    def get(self, request, n=10):
        try:
            n = int(n)
        except ValueError:
            return Response({"error": "Invalid number specified."}, status=400)

        if n <= 0:
            return Response({"error": "Number must be greater than zero."}, status=400)

        movies = Movie.objects.order_by('-rating', '-metascore')[:n]
        serializer = BestMovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ActorBirthdayView(APIView):
    def get(self, request, date):
        try:
            input_date = datetime.strptime(date, "%d%m%Y").date()
        except ValueError:
            return Response({"error": "Invalid date format. Please use DDMMYYYY."}, status=400)
        closest_actors = []
        smallest_difference = timedelta.max
        actors = get_all_actors()
        valid_date_found = False
        for actor in actors:
            try:
                actor_birthday = actor.date  # actor.birthdate is in "YYYY-MM-DD" format
                actor_birthday = datetime.strptime(actor_birthday, "%Y-%m-%d").date()
                valid_date_found = True
            except ValueError:
                continue

            difference = abs(actor_birthday - input_date)
            if difference <= smallest_difference:
                if difference < smallest_difference:
                    closest_actors = [] 
                closest_actors.append({"date": actor_birthday.strftime("%d%m%Y"),
                                       "actorname": actor.name})
                smallest_difference = difference

        if not valid_date_found:
            return Response({"error": "No valid actor birthdays found in the database."}, status=404)

        if closest_actors:
            return Response(closest_actors)
        else:
            return Response({"error": "No actor found with a birthday close to the provided date."}, status=404)