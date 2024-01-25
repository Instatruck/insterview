from rest_framework import serializers
from pages.models import Movie, Actor, Director
from django.utils.text import slugify

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    rating = serializers.FloatField()


class ActorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    birthdate = serializers.DateField(source='date')
    birthplace = serializers.CharField(source="place",max_length=100)
    films = serializers.SerializerMethodField()

    def get_films(self, obj):
        request = self.context.get('request')
        if request:
            actor_slug = slugify(obj.name)
            return request.build_absolute_uri(f'/actors/{actor_slug}/films/')
        return None



class DirectorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    birthdate = serializers.DateField(source='date')
    birthplace = serializers.CharField(source="place",max_length=100)
    films = serializers.SerializerMethodField()

    def get_films(self, obj):
        request = self.context.get('request')
        if request:
            director_slug = slugify(obj.name)
            return request.build_absolute_uri(f'/directors/{director_slug}/films/')
        return None
