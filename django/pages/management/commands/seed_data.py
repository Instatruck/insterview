
from django.core.management.base import BaseCommand
from pages.models import *
import django

# Apply for seed and test 
def SeedData():
    director1 = Director.objects.create(
                name="Director 1",
                date="01011975",
                place="Los Angeles, CA",
                masterpiece="Best Movie Ever",
                award_win=3,
                award_nom=5,
                person_link="https://example.com/director1",
                award_link="https://example.com/director1/awards"
            )

    director2 = Director.objects.create(
        name="Director 2",
        date="02022012",
        place="New York, NY",
        masterpiece="Greatest Film of All Time",
        award_win=5,
        award_nom=7,
        person_link="https://example.com/director2",
        award_link="https://example.com/director2/awards"
    )

    director3 = Director.objects.create(
        name="Director 3",
        date="02121999",
        place="New York, NY",
        masterpiece="Something Amazing",
        award_win=1,
        award_nom=4,
        person_link="https://example.com/director3",
        award_link="https://example.com/director3/awards"
    )

    # Create Actor instances
    actor1 = Actor.objects.create(
        name="Actor 1",
        date="03031970",
        place="Chicago, IL",
        masterpiece="Oscar-Winning Performance",
        award_win=2,
        award_nom=4,
        person_link="https://example.com/actor1",
        award_link="https://example.com/actor1/awards"
    )

    actor2 = Actor.objects.create(
        name="Actor 2",
        date="04041985",
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

    movie3 = Movie.objects.create(
        movieid=3,
        year=2020,
        rank=5,
        title="Sample Movie 3",
        description="Another sample movie description.",
        duration=80,
        genres="Comedy",
        rating=7.8,
        metascore=80,
        votes=800,
        gross_earning_in_mil=42.0,
        director=director3,
        actor=actor2
    )

    movie4 = Movie.objects.create(
        movieid=4,
        year=2017,  # Change the year as needed
        rank=4,  # Change other attributes as needed
        title="Movie 4",
        description="Description for Movie 4.",
        duration=110,
        genres="Drama",
        rating=8.0,
        metascore=88,
        votes=1100,
        gross_earning_in_mil=90.0,
        director=director2,  # Change the director as needed
        actor=actor1  # Change the actor as needed
    )

    # Create Movie 5
    movie5 = Movie.objects.create(
        movieid=5,
        year=2016,  # Change the year as needed
        rank=3,  # Change other attributes as needed
        title="Movie 5",
        description="Description for Movie 5.",
        duration=105,
        genres="Action",
        rating=7.9,
        metascore=82,
        votes=1050,
        gross_earning_in_mil=85.5,
        director=director1,  # Change the director as needed
        actor=actor2  # Change the actor as needed
    )

    # Create Movie 6
    movie6 = Movie.objects.create(
        movieid=6,
        year=2015,  # Change the year as needed
        rank=2,  # Change other attributes as needed
        title="Movie 6",
        description="Description for Movie 6.",
        duration=120,
        genres="Comedy",
        rating=7.7,
        metascore=75,
        votes=950,
        gross_earning_in_mil=78.0,
        director=director3,  # Change the director as needed
        actor=actor2  # Change the actor as needed
    )

    # Create Movie 7
    movie7 = Movie.objects.create(
        movieid=7,
        year=2005,  # Change the year as needed
        rank=4,  # Change other attributes as needed
        title="Movie 7",
        description="Description for Movie 7.",
        duration=90,
        genres="Comedy",
        rating=6,
        metascore=50,
        votes=1000,
        gross_earning_in_mil=50.0,
        director=director3,  # Change the director as needed
        actor=actor2  # Change the actor as needed
    )

    # Create Movie 8
    movie8 = Movie.objects.create(
        movieid=8,
        year=1997,  # Change the year as needed
        rank=4,  # Change other attributes as needed
        title="Movie 8",
        description="Description for Movie 8.",
        duration=120,
        genres="Comedy",
        rating=9,
        metascore=90,
        votes=10,
        gross_earning_in_mil=12.0,
        director=director1,  # Change the director as needed
        actor=actor2  # Change the actor as needed
    )

    # Create Movie 9
    movie9 = Movie.objects.create(
        movieid=9,
        year=2001,  # Change the year as needed
        rank=92,  # Change other attributes as needed
        title="Movie 9",
        description="Description for Movie 9.",
        duration=150,
        genres="Comedy",
        rating=10,
        metascore=100,
        votes=2,
        gross_earning_in_mil=650.0,
        director=director3,  # Change the director as needed
        actor=actor1  # Change the actor as needed
    )

    # Create Movie 10
    movie10 = Movie.objects.create(
        movieid=10,
        year=2018,  # Change the year as needed
        rank=50,  # Change other attributes as needed
        title="Movie 10",
        description="Description for Movie 10.",
        duration=120,
        genres="Comedy",
        rating=2,
        metascore=20,
        votes=5,
        gross_earning_in_mil=12.0,
        director=director3,  # Change the director as needed
        actor=actor2  # Change the actor as needed
    )

    # Create Movie 11
    movie11 = Movie.objects.create(
        movieid=11,
        year=2017,  # Change the year as needed
        rank=58,  # Change other attributes as needed
        title="Movie 11",
        description="Description for Movie 11.",
        duration=60,
        genres="Comedy",
        rating=50,
        metascore=70,
        votes=6,
        gross_earning_in_mil=127.0,
        director=director2,  # Change the director as needed
        actor=actor1  # Change the actor as needed
    )
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        print('------ SEEDING DATA ------')
        # Create Director instances
        try:
            SeedData()
            print('-> Complete')
        except:
            print('-> Something went wrong while seeding data. Could be the seed data alrady exists')
            pass