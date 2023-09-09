from behave import given, when, then
from django.urls import reverse
from rest_framework import status
from pages.models import Movie  # Import your Movie model
from pages.serializers import MovieSerializer  # Import your MovieSerializer

@given('I am using the movie API')
def step_given_movie_api(context):
    pass  # No specific action needed for this step

@when("I access the '/movies/best/<n>' endpoint")
def step_when_access_best_movies(context):
    url = reverse('best_movie_with_count', kwargs={'count': 3})
    context.response = context.test.client.get(url)
    context.test.assertEqual(context.response.status_code, status.HTTP_200_OK)

@then('the API only shows me the movies {movielist} sorted by rating and then by metascore')
def step_then_api_show_movies(context, movielist):
    context.test.assertEqual(context.response.status_code, status.HTTP_200_OK)
    
    # Retrieve and serialize the expected movies based on the scenario
    list_movies = Movie.objects.all().order_by('-rating', '-metascore')[:3]

    expected_data = MovieSerializer(list_movies, many=True).data
    actual_data = context.response.data['data']

    context.test.assertEqual(expected_data, actual_data)

@when("I access the '/movies/best/' endpoint")
def step_when_access_top_10_movies(context):
    url = reverse('best_movie')
    context.response = context.test.client.get(url)
    context.test.assertEqual(context.response.status_code, status.HTTP_200_OK)

@then('the API shows me the top 10 movies sorted by rating and then by metascore')
def step_then_api_show_top_10_movies(context):
    context.test.assertEqual(context.response.status_code, status.HTTP_200_OK)

    # Retrieve and serialize the top 10 movies
    list_movies = Movie.objects.all().order_by('-rating', '-metascore')[:10]
    expected_data = MovieSerializer(list_movies, many=True).data
    actual_data = context.response.data['data']

    context.test.assertEqual(expected_data, actual_data)
