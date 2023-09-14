from rest_framework import serializers
from .models import Movie, Director, Actor
from utils.tools import sanitize_to_slug
from pages.constant import FE_MOVIE_BASE_URL

def DataHandlerForPeople(data, is_actor):
    if is_actor:
        filter = {'actor_id': data['name']}
    else:
        filter = {'director_id': data['name']}

    list_of_films = Movie.objects.filter(**filter)
    list_film_links = []
    for i in list_of_films:
        list_film_links.append(FE_MOVIE_BASE_URL + sanitize_to_slug(i.title))
    data['films'] = list_film_links
    data['birthday'] = data.pop('date', None)
    data['birthplace'] = data.pop('place', None)
    return data
    
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'date', 'place']
    
    def to_representation(self, instance):
        return DataHandlerForPeople(super().to_representation(instance), is_actor=False)

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'date', 'place']

    def to_representation(self, instance):
        return DataHandlerForPeople(super().to_representation(instance), is_actor=True)

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'rating']

class MovieLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        link = FE_MOVIE_BASE_URL + sanitize_to_slug(data['title'])
        return link

class DateFilteringSerializer(serializers.Serializer):
    start_year = serializers.IntegerField(allow_null=True, required=False)
    end_year = serializers.IntegerField(allow_null=True, required=False)

class CloseToBirthdayRequestSerializer(serializers.Serializer):
    date = serializers.DateField(format='%Y-%m-%d')