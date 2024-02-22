from rest_framework.test import APITestCase

from pages.models import Movie, Actor, Director

MOVIE1_DATA = {
    'movieid': 1,
    'year': 2008,
    'title': 'Iron Man',
    'description': (
        'After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique '
        'weaponized suit of armor to fight evil.'
    ),
    'genres': 'Action',
    'rating': 7.9,
    'metascore': 79,
}
MOVIE2_DATA = {
    'movieid': 2,
    'year': 2021,
    'title': 'Spider-Man: No Way Home',
    'description': (
        'When a spell goes wrong, dangerous foes from other worlds start to appear, forcing Peter '
        'to discover what it truly means to be Spider-Man.'
    ),
    'genres': 'Action',
    'rating': 8.2,
    'metascore': 71,
}
MOVIE3_DATA = {
    'movieid': 3,
    'year': 1972,
    'title': 'The Godfather',
    'description': (
        'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his '
        'reluctant son.'
    ),
    'genres': 'Crime',
    'rating': 9.2,
    'metascore': 100,
}
MOVIE4_DATA = {
    'movieid': 4,
    'year': 1939,
    'title': 'Gone with the Wind',
    'description': (
        'A sheltered and manipulative Southern belle and a roguish profiteer face off in a turbulent romance as the '
        'society around them crumbles with the end of slavery and is rebuilt during the Civil War and Reconstruction '
        'periods.'
    ),
    'genres': 'Drama',
    'rating': 8.2,
    'metascore': 97,
}


ACTOR1_DATA = {
    'name': 'Robert Downey Jr.',
    'date': '04041965',
    'place': 'New York, US',
}
ACTOR2_DATA = {
    'name': 'Tom Holland',
    'date': '01061996',
    'place': 'London, England',
}
ACTOR3_DATA = {
    'name': 'Marlon Brando',
    'date': '03041924',
    'place': 'Nebraska, US',
}

DIRECTOR1_DATA = {
    'name': 'Jon Favreau',
    'date': 'October 19, 1966',
    'place': 'New York, US',
}
DIRECTOR2_DATA = {
    'name': 'Jon Watts',
    'date': 'June 28, 1981',
    'place': 'Colorado, US',
}


class MovieTest(APITestCase):
    base_url = '/movies/'

    def setUp(self):
        self.movie1 = Movie.objects.create(**MOVIE1_DATA)
        self.movie2 = Movie.objects.create(**MOVIE2_DATA)

    def test_get_all_movies(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.data, [
            {
                'title': self.movie1.title,
                'year': self.movie1.year,
                'description': self.movie1.description,
                'rating': self.movie1.rating,
            },
            {
                'title': self.movie2.title,
                'year': self.movie2.year,
                'description': self.movie2.description,
                'rating': self.movie2.rating,
            }
        ])

    def test_filter_movies_by_start_year(self):
        response = self.client.get(self.base_url, QUERY_STRING=f'start_year=2007')
        self.assertEqual(len(response.data), 2)

        response = self.client.get(self.base_url, QUERY_STRING='start_year=2008')
        self.assertEqual(len(response.data), 2)

        response = self.client.get(self.base_url, QUERY_STRING='start_year=2009')
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.base_url, QUERY_STRING='start_year=2021')
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.base_url, QUERY_STRING='start_year=2022')
        self.assertEqual(len(response.data), 0)

    def test_filter_movies_by_end_year(self):
        response = self.client.get(self.base_url, QUERY_STRING=f'end_year=2007')
        self.assertEqual(len(response.data), 0)

        response = self.client.get(self.base_url, QUERY_STRING=f'end_year=2008')
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.base_url, QUERY_STRING=f'end_year=2009')
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.base_url, QUERY_STRING=f'end_year=2021')
        self.assertEqual(len(response.data), 2)

        response = self.client.get(self.base_url, QUERY_STRING=f'end_year=2022')
        self.assertEqual(len(response.data), 2)

    def test_filter_movies_by_start_year_and_end_year(self):
        response = self.client.get(self.base_url, QUERY_STRING=f'start_year=2007&end_year=2007')
        self.assertEqual(len(response.data), 0)

        response = self.client.get(self.base_url, QUERY_STRING=f'start_year=2007&end_year=2008')
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.base_url, QUERY_STRING=f'start_year=2007&end_year=2009')
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.base_url, QUERY_STRING=f'start_year=2007&end_year=2021')
        self.assertEqual(len(response.data), 2)

        response = self.client.get(self.base_url, QUERY_STRING=f'start_year=2007&end_year=2022')
        self.assertEqual(len(response.data), 2)

        response = self.client.get(self.base_url, QUERY_STRING=f'start_year=2022&end_year=2022')
        self.assertEqual(len(response.data), 0)

    
class TopMovieTest(APITestCase):
    base_url = '/movies/best/'

    def setUp(self):
        self.movie1 = Movie.objects.create(**MOVIE1_DATA)
        self.movie2 = Movie.objects.create(**MOVIE2_DATA)
        self.movie3 = Movie.objects.create(**MOVIE3_DATA)
        self.movie4 = Movie.objects.create(**MOVIE4_DATA)

    def test_get_top_n_movies(self):
        response = self.client.get(f'{self.base_url}1/')
        # The Godfather
        self.assertEqual(response.data, [
            {
                'title': self.movie3.title,
                'year': self.movie3.year,
                'description': self.movie3.description,
                'rating': self.movie3.rating,
            }
        ])

        response = self.client.get(f'{self.base_url}3/')
        # The Godfather, Gone with the Wind, Spider-Man: No Way Home (Gone with the Wind has the same rating with
        # Spider-Man: No Way Home)
        self.assertEqual(response.data, [
            {
                'title': self.movie3.title,
                'year': self.movie3.year,
                'description': self.movie3.description,
                'rating': self.movie3.rating,
            },
            {
                'title': self.movie4.title,
                'year': self.movie4.year,
                'description': self.movie4.description,
                'rating': self.movie4.rating,
            },
            {
                'title': self.movie2.title,
                'year': self.movie2.year,
                'description': self.movie2.description,
                'rating': self.movie2.rating,
            },
        ])

    def test_get_top_n_movies_when_n_is_greater_than_total_movies(self):
        # Ask for top 5 while there are only 4 in the DB --> should return 4
        response = self.client.get(f'{self.base_url}5/')
        self.assertEqual(len(response.data), 4)

    def test_get_top_10_movies(self):
        response = self.client.get(self.base_url)
        # There are 4 items in the DB --> should return all
        self.assertEqual(response.data, [
            {
                'title': self.movie3.title,
                'year': self.movie3.year,
                'description': self.movie3.description,
                'rating': self.movie3.rating,
            },
            {
                'title': self.movie4.title,
                'year': self.movie4.year,
                'description': self.movie4.description,
                'rating': self.movie4.rating,
            },
            {
                'title': self.movie2.title,
                'year': self.movie2.year,
                'description': self.movie2.description,
                'rating': self.movie2.rating,
            },
            {
                'title': self.movie1.title,
                'year': self.movie1.year,
                'description': self.movie1.description,
                'rating': self.movie1.rating,
            }
        ])

    def test_get_top_10_movies_when_total_movies_is_greater_than_10(self):
        # Create additional 10 movies --> there are 14 movies
        for i in range(10):
            data = {
                'movieid': 5 + i,
                'year': 2000,
                'title': 'Test',
                'description': '',
                'genres': 'Test',
                'rating': 5.0,
                'metascore': 80,
            }
            Movie.objects.create(**data)

        self.assertEqual(Movie.objects.count(), 14)

        response = self.client.get(self.base_url)
        self.assertEqual(len(response.data), 10)


class ActorTest(APITestCase):
    base_url = '/actors/'

    def setUp(self):
        self.actor1 = Actor.objects.create(**ACTOR1_DATA)
        self.actor2 = Actor.objects.create(**ACTOR2_DATA)

        Movie.objects.create(
            **MOVIE1_DATA,
            actor=self.actor1
        )

    def test_get_all_actors(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.data, [
            {
                'name': self.actor1.name,
                'date': self.actor1.date,
                'place': self.actor1.place,
                'films': f'/actors/{self.actor1.name}/films/',
            },
            {
                'name': self.actor2.name,
                'date': self.actor2.date,
                'place': self.actor2.place,
                'films': f'/actors/{self.actor2.name}/films/',
            },
        ])

    def test_get_all_films(self):
        response = self.client.get(f'{self.base_url}{self.actor1.pk}/films/')
        self.assertEqual(len(response.data), 1)


class ActorNearestToBirthdayTest(APITestCase):
    base_url = '/actors/birthdays/'

    def setUp(self):
        self.actor1 = Actor.objects.create(**ACTOR1_DATA)
        self.actor2 = Actor.objects.create(**ACTOR2_DATA)
        self.actor3 = Actor.objects.create(**ACTOR3_DATA)

    def test_get_actors_with_nearest_birthdays(self):
        date = '05101995'
        response = self.client.get(f'{self.base_url}{date}/')
        self.assertEqual(response.data, [
            {
                'name': self.actor2.name,
                'date': self.actor2.date,
                'place': self.actor2.place,
                'films': f'/actors/{self.actor2.name}/films/',
            },
            {
                'name': self.actor1.name,
                'date': self.actor1.date,
                'place': self.actor1.place,
                'films': f'/actors/{self.actor1.name}/films/',
            },
            {
                'name': self.actor3.name,
                'date': self.actor3.date,
                'place': self.actor3.place,
                'films': f'/actors/{self.actor3.name}/films/',
            },
        ])


class DirectorTest(APITestCase):
    base_url = '/directors/'

    def setUp(self):
        self.director1 = Director.objects.create(**DIRECTOR1_DATA)
        self.director2 = Director.objects.create(**DIRECTOR2_DATA)

        Movie.objects.create(
            **MOVIE1_DATA,
            director=self.director1
        )

    def test_get_all_directors(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.data, [
            {
                'name': self.director1.name,
                'date': self.director1.date,
                'place': self.director1.place,
                'films': '/directors/Jon Favreau/films/',
            },
            {
                'name': self.director2.name,
                'date': self.director2.date,
                'place': self.director2.place,
                'films': '/directors/Jon Watts/films/',
            },
        ])

    def test_get_all_films(self):
        response = self.client.get(f'{self.base_url}{self.director1.pk}/films/')
        self.assertEqual(len(response.data), 1)
