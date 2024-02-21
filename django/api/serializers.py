from rest_framework import serializers

from pages.models import (
    Movie,
    Actor,
    Director,
)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'rating']


class ActorSerializer(serializers.ModelSerializer):
    films = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ['name', 'date', 'place', 'films']

    def get_films(self, actor):
        return f'/actors/{actor.pk}/films/'


class DirectorSerializer(serializers.ModelSerializer):
    films = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['name', 'date', 'place', 'films']

    def get_films(self, director):
        return f'/directors/{director.pk}/films/'
