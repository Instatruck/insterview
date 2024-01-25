from django.db import models


class Movie(models.Model):
    year = models.IntegerField()
    rank = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True, blank=True)
    duration = models.IntegerField(blank=True, null=True)
    genres = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    metascore = models.IntegerField(blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    gross_earning_in_mil = models.FloatField(blank=True, null=True)
    # Use ForeignKey for a simple one-to-one relationship as requirements
    # Here we can do manytomany
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True, blank=True)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'movie'

class Director(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=500, null=True)
    masterpiece = models.CharField(max_length=500, null=True)
    award_win = models.IntegerField(blank=True, null=True)
    award_nom = models.IntegerField(blank=True, null=True)
    person_link = models.URLField(max_length=500, null=True)
    award_link = models.URLField(max_length=500, null=True)
    
    class Meta:
        db_table = 'director'

class Actor(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=500, null=True)
    masterpiece = models.CharField(max_length=500, null=True)
    award_win = models.IntegerField(blank=True, null=True)
    award_nom = models.IntegerField(blank=True, null=True)
    person_link = models.URLField(max_length=500, null=True)
    award_link = models.URLField(max_length=500, null=True)
    
    class Meta:
        db_table = 'actor'
