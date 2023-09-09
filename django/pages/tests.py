from django.test import TestCase
from pages.management.commands.seed_data import SeedData
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from pages.models import Movie, Director, Actor 
from pages.serializers import MovieSerializer, DirectorSerializer, ActorSerializer, MovieLinkSerializer
from django.core.paginator import Paginator
# Create your tests here.
class APITest(TestCase):
    def setUp(self):
        SeedData()

    def test_get_list_movies(self):
        url = reverse('movie') + f'?page=1&page-size=5'
        response = self.client.get(url)
        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test pagination
        self.assertEqual(5, len(response.data['data']))

        # Test data
        all_movies = Movie.objects.filter().all().order_by('movieid')
        paginator = Paginator(all_movies, 5)
        data = paginator.page(1).object_list
        data = MovieSerializer(data, many=True).data
        self.assertEqual(data, response.data['data'])

    def test_get_list_directors(self):
        url = reverse('director') + f'?page=1&page-size=1'
        response = self.client.get(url)
        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test pagination
        self.assertEqual(1, len(response.data['data']))

        # Test data
        all_movies = Director.objects.filter().all().order_by('name')
        paginator = Paginator(all_movies, 1)
        data = paginator.page(1).object_list
        data = DirectorSerializer(data, many=True).data
        self.assertEqual(data, response.data['data'])

    def test_get_list_actors(self):
        url = reverse('actor') + f'?page=1&page-size=1'
        response = self.client.get(url)
        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test pagination
        self.assertEqual(1, len(response.data['data']))

        # Test data
        all_movies = Actor.objects.filter().all().order_by('name')
        paginator = Paginator(all_movies, 1)
        data = paginator.page(1).object_list
        data = ActorSerializer(data, many=True).data
        self.assertEqual(data, response.data['data'])

    def test_get_list_actor_films(self):
        actor = Actor.objects.first()
        actor_pk = actor.name
        
        url = reverse('actor_films', kwargs={'id': actor_pk} ) + f'?page=1&page-size=1'
        response = self.client.get(url)

        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test pagination
        self.assertEqual(1, len(response.data['data']))

        # Test data
        list_movies = Movie.objects.filter(actor=actor).order_by('movieid')
        paginator = Paginator(list_movies, 1)
        data = paginator.page(1).object_list
        data = MovieLinkSerializer(data, many=True).data
        self.assertEqual(data, response.data['data'])

    def test_get_list_director_films(self):
        director = Director.objects.first()
        director_pk = director.name

        url = reverse('director_films', kwargs={'id': director_pk} ) + f'?page=1&page-size=1'
        response = self.client.get(url)

        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test pagination
        self.assertEqual(1, len(response.data['data']))

        # Test data
        list_movies = Movie.objects.filter(director=director).order_by('movieid')
        paginator = Paginator(list_movies, 1)
        data = paginator.page(1).object_list
        data = MovieLinkSerializer(data, many=True).data
        self.assertEqual(data, response.data['data'])

#  path('movies/', views.MovieAPI.as_view(), name = 'movie'),
#     path('directors/', views.DirectorAPI.as_view(), name = 'director'),
#     path('actors/', views.ActorAPI.as_view(), name = 'actor'),
#       actors/<str:id>/films/', views.ActorFilmsAPI.as_view(), name = 'actor_films'),
#     path('directors/<str:id>/films/', views.DirectorFilmsAPI.as_view(), name = 'director_films'),