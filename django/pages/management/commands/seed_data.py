
from django.core.management.base import BaseCommand
from pages.models import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        print('------ SEEDING DATA ------')
            # Create Director instances
        director1 = Director.objects.create(
            name="Director 1",
            date="January 1, 1980",
            place="Los Angeles, CA",
            masterpiece="Best Movie Ever",
            award_win=3,
            award_nom=5,
            person_link="https://example.com/director1",
            award_link="https://example.com/director1/awards"
        )

        director2 = Director.objects.create(
            name="Director 2",
            date="February 2, 1990",
            place="New York, NY",
            masterpiece="Greatest Film of All Time",
            award_win=5,
            award_nom=7,
            person_link="https://example.com/director2",
            award_link="https://example.com/director2/awards"
        )

        # Create Actor instances
        actor1 = Actor.objects.create(
            name="Actor 1",
            date="March 3, 1970",
            place="Chicago, IL",
            masterpiece="Oscar-Winning Performance",
            award_win=2,
            award_nom=4,
            person_link="https://example.com/actor1",
            award_link="https://example.com/actor1/awards"
        )

        actor2 = Actor.objects.create(
            name="Actor 2",
            date="April 4, 1985",
            place="Miami, FL",
            masterpiece="Critically Acclaimed Role",
            award_win=1,
            award_nom=3,
            person_link="https://example.com/actor2",
            award_link="https://example.com/actor2/awards"
        )

        # Create Movie instances
        movie1 = Movie.objects.create(
            movieid=1,
            year=2023,
            rank=1,
            title="Sample Movie 1",
            description="A sample movie description.",
            duration=120,
            genres="Action, Adventure",
            rating=8.5,
            metascore=85,
            votes=1000,
            gross_earning_in_mil=50.5,
            director=director1,
            actor=actor1
        )

        movie2 = Movie.objects.create(
            movieid=2,
            year=2023,
            rank=2,
            title="Sample Movie 2",
            description="Another sample movie description.",
            duration=110,
            genres="Comedy",
            rating=7.8,
            metascore=80,
            votes=800,
            gross_earning_in_mil=42.0,
            director=director2,
            actor=actor2
        )