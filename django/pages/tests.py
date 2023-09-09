from django.test import TestCase
from pages.management.commands.seed_data import SeedData
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from pages.models import Movie, Director, Actor 
from pages.serializers import MovieSerializer, DirectorSerializer, ActorSerializer, MovieLinkSerializer
from django.core.paginator import Paginator
from datetime import datetime
from utils.tools import parse_date
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

    def test_get_list_movies_with_filtering(self):
        url = reverse('movie') + f'?page=1&page-size=100&start_year=1900&end_year=2022'
        response = self.client.get(url)
        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test pagination
        self.assertEqual(9, len(response.data['data']))

        # Test data
        all_movies = Movie.objects.filter(year__gte=1900, year__lte=2022).all().order_by('movieid')
        paginator = Paginator(all_movies, 100)
        data = paginator.page(1).object_list
        data = MovieSerializer(data, many=True).data
        self.assertEqual(data, response.data['data'])

    def test_get_list_movies_with_filtering_but_wrong_data(self):
        url = reverse('movie') + f'?page=1&page-size=5&start_year=wrong_type&end_year=wrong_type'
        response = self.client.get(url)
        # Test API call
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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


    def test_best_movie_with_count(self):
        url = reverse('best_movie_with_count', kwargs={'count': 1} )
        response = self.client.get(url)

        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test count data
        self.assertEqual(1, len(response.data['data']))

        # Test data
        list_movies = Movie.objects.all().order_by('-rating', '-metascore')[:1]
        data = MovieSerializer(list_movies, many=True).data
        self.assertEqual(data, response.data['data'])

    def test_best_movie(self):
        url = reverse('best_movie')
        response = self.client.get(url)

        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test count data
        self.assertEqual(10, len(response.data['data']))

        # Test data
        list_movies = Movie.objects.all().order_by('-rating', '-metascore')[:10]
        data = MovieSerializer(list_movies, many=True).data
        self.assertEqual(data, response.data['data'])

    def test_closet_to_actor_birthday(self):
        url = reverse('closet-to-actors-birthday', kwargs={'date': '2023-01-01'}) + f'?page=1&page-size=2'
        response = self.client.get(url)

        # Test API call
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test count data
        self.assertEqual(2, len(response.data['data']))

        # Test data
        user_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
        list_actors = Actor.objects.all()
        actors_with_dates = []
        for actor in list_actors:
            parsed_date = parse_date(actor.date)
            if parsed_date is not None:
                date_difference = abs(parsed_date - user_date)
                actors_with_dates.append((actor, date_difference))
        actors_with_dates.sort(key=lambda x: x[1])

        sorted_actors = [actor[0] for actor in actors_with_dates]
        paginator = Paginator(sorted_actors, 2)
        data = paginator.page(1).object_list
        data = ActorSerializer(data, many=True).data
        self.assertEqual(data, response.data['data'])
    