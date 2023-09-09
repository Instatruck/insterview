import os
import django
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Max, Min
from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from .forms import MovieForm
from .serializers import (
    DirectorSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieLinkSerializer,
    DateFilteringSerializer,
    CloseToBirthdayRequestSerializer,
)
from rest_framework.views import APIView
from rest_framework import status
from utils.response import CustomResponse
from utils.tools import parse_date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
django.setup()


def home(request):
    return render(request, "home.html", {})


def clean_string_list(stringa):
    """Utility function, to improve formatting in 'masterpiece' column.
    Change "['Enter the Void', 'Druid Peak', 'Blinders', 'Boys on Film X']" into
    'Enter the Void, Druid Peak, Blinders, Boys on Film X'
    """
    bad_chars = "[]\"\"\'\'"
    for c in bad_chars:
        stringa = stringa.replace(c, "")
    return stringa


class DirectorAPI(APIView):
    def get(self, request):
        page, page_size = GetPageAndPageSizeFromReuest(request)
        all_directors = Director.objects.all().order_by('name')
        paginator = Paginator(all_directors, page_size)
        data = paginator.page(page).object_list
        return CustomResponse(status_code=status.HTTP_200_OK, data=DirectorSerializer(data, many=True).data, pagination=paginator, page=page, page_size=page_size).to_json_response()


class MovieAPI(APIView):
    serializer_class = DateFilteringSerializer

    def get(self, request):
        page, page_size = GetPageAndPageSizeFromReuest(request)
        serializer = self.serializer_class(data=request.GET)
        if not serializer.is_valid():
            errors = serializer.errors
            return CustomResponse(status_code=status.HTTP_400_BAD_REQUEST, message=errors).to_json_response()

        filtering = {}
        if serializer.data['start_year'] != None:
            filtering['year__gte'] = serializer.data['start_year']
        if serializer.data['end_year'] != None:
            filtering['year__lte'] = serializer.data['end_year']

        all_movies = Movie.objects.filter(
            **filtering).all().order_by('movieid')
        paginator = Paginator(all_movies, page_size)
        try:
            data = paginator.page(page).object_list
        except:
            data = []
        return CustomResponse(status_code=status.HTTP_200_OK, data=MovieSerializer(data, many=True).data, pagination=paginator, page=page, page_size=page_size).to_json_response()


class ActorAPI(APIView):
    def get(self, request):
        page, page_size = GetPageAndPageSizeFromReuest(request)
        all_actors = Actor.objects.all().order_by('name')
        paginator = Paginator(all_actors, page_size)
        data = paginator.page(page).object_list
        return CustomResponse(status_code=status.HTTP_200_OK, data=ActorSerializer(data, many=True).data, pagination=paginator, page=page, page_size=page_size).to_json_response()


class ActorFilmsAPI(APIView):
    def get(self, request, id):
        page, page_size = GetPageAndPageSizeFromReuest(request)
        actor = Actor.objects.filter(pk=id).first()
        if not actor:
            return CustomResponse(status_code=status.HTTP_400_BAD_REQUEST, message="actor id not found").to_json_response()
        list_movies = Movie.objects.filter(actor=actor).order_by('movieid')
        paginator = Paginator(list_movies, page_size)
        data = paginator.page(page).object_list
        return CustomResponse(status_code=status.HTTP_200_OK, data=MovieLinkSerializer(data, many=True).data, pagination=paginator, page=page, page_size=page_size).to_json_response()


class DirectorFilmsAPI(APIView):
    def get(self, request, id):
        page, page_size = GetPageAndPageSizeFromReuest(request)
        director = Director.objects.filter(pk=id).first()
        if not director:
            return CustomResponse(status_code=status.HTTP_400_BAD_REQUEST, message="actor id not found").to_json_response()
        list_movies = Movie.objects.filter(
            director=director).order_by('movieid')
        paginator = Paginator(list_movies, page_size)
        data = paginator.page(page).object_list
        return CustomResponse(status_code=status.HTTP_200_OK, data=MovieLinkSerializer(data, many=True).data, pagination=paginator, page=page, page_size=page_size).to_json_response()


class BestMoviesAPI(APIView):
    def get(self, request, count=None):
        if count is None:
            limit = 10
        else:
            if not isinstance(count, int):
                return CustomResponse(status_code=status.HTTP_400_BAD_REQUEST, message="the count of best records is not a valid number").to_json_response()
            else:
                if int(count) <= 0:
                    return CustomResponse(status_code=status.HTTP_400_BAD_REQUEST, message="the count of best records must be greater than 0").to_json_response()
                else:
                    limit = int(count)

        # Best movies have high rating and metarscore so need to order desc
        list_movies = Movie.objects.all().order_by(
            '-rating', '-metascore')[:limit]
        return CustomResponse(status_code=status.HTTP_200_OK, data=MovieSerializer(list_movies, many=True).data).to_json_response()

class ClosetToActorBirthday(APIView):
    serializer_class=CloseToBirthdayRequestSerializer
    def get(self, request, date):
        page, page_size = GetPageAndPageSizeFromReuest(request)
        try:
            user_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return CustomResponse(status_code=status.HTTP_400_BAD_REQUEST, message="user's birthday input must follow the format of %Y-%m-%d, for example: 2021-12-29").to_json_response()

        list_actors = Actor.objects.all()
        actors_with_dates = []
        for actor in list_actors:
            parsed_date = parse_date(actor.date)
            if parsed_date is not None:
                date_difference = abs(parsed_date - user_date)
                actors_with_dates.append((actor, date_difference))
        actors_with_dates.sort(key=lambda x: x[1])

        sorted_actors = [actor[0] for actor in actors_with_dates]
        paginator = Paginator(sorted_actors, page_size)
        data = paginator.page(page).object_list
        return CustomResponse(status_code=status.HTTP_200_OK, data=ActorSerializer(data, many=True).data, pagination=paginator, page=page, page_size=page_size).to_json_response()
        

def director(request):
    base_dir = os.path.abspath(__file__)
    for i in range(3):  
        base_dir = os.path.dirname(base_dir)
    all_director = Director.objects.all()
    paginator = Paginator(all_director, 50)
    page = request.GET.get('page')
    directors = paginator.get_page(page)

    return render(request, "director.html", {'Director': directors})


def movie(request):
    base_dir = os.path.abspath(__file__)
    for i in range(3):
        base_dir = os.path.dirname(base_dir)
    all_movies = Movie.objects.all()
    paginator = Paginator(all_movies, 50)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    return render(request, "movie.html", {'Movie': movies})


def actor(request):
    base_dir = os.path.abspath(__file__)
    for i in range(3):
        base_dir = os.path.dirname(base_dir)
    all_actor = Actor.objects.all()
    paginator = Paginator(all_actor, 50)
    page = request.GET.get('page')
    actors = paginator.get_page(page)
    return render(request, "actor.html", {'Actor': actors})

def recommendation(request):
    return render(request, "recommendation.html", {})


def insert_data(request):
    return render(request, "insert_data.html", {})


def insert_data_submission(request):
    year = request.POST["year"]
    title = request.POST["title"]
    genres = request.POST["type"]
    descrption = request.POST["description"]
    director_name = request.POST["director"]
    actor_name = request.POST["actor"]

    new_actor = Actor(name=actor_name)
    new_director = Director(name=director_name)

    new_actor.save()
    new_director.save()

    director_name = Director.objects.get(name=director_name)
    actor_name = Actor.objects.get(name=actor_name)

    new_movie = Movie(title=title, year=year, genres=genres, description=descrption, director=director_name,
                      actor=actor_name)
    new_movie.save()
    return render(request, "insert_data.html", {})


def edit_movie(request, pk):
    post = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your movie has been updated!')
        except Exception as e:
            messages.warning(
                request, 'Your movie was not updated: Error {}'.format(e))
    else:
        form = MovieForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, "new_movie.html", context)


def new_movie(request):
    template = 'new_movie.html'
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, template, context)


def delete_movie(request, pk):
    post = get_object_or_404(Movie, pk=pk)
    try:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=post)
            post.delete()
            messages.success(
                request, 'You have successfully deleted the movie')
        else:
            form = MovieForm(instance=post)
    except Exception as e:
        messages.warning(
            request, 'The movie cannot be deleted: Error {}'.format(e))
    context = {
        'form': form,
        'post': post
    }
    return render(request, "new_movie.html", context)


def search(request):
    template = 'recommendation.html'

    query = request.GET.get('q')
    tep = "%%%s%%" % query
    filter_title = Director.objects.raw(
        "SELECT m.title AS title, d.name AS name, a.name AS star \
        FROM pages_director AS d LEFT JOIN pages_movie AS m ON d.name = m.director_id \
        LEFT JOIN pages_actor AS a ON a.name = m.actor_id \
        WHERE m.title LIKE %s", [tep])

    filter_data = Director.objects.raw(
        "SELECT m.title AS title, m.rating AS rating, m.votes AS votes, m.metascore AS metascore, \
        m.gross_earning_in_mil AS gross, d.name AS name, d.award_win AS d_win, d.award_nom AS d_nom, \
        a.name AS star, a.award_win AS a_win, a.award_nom AS a_nom \
        FROM pages_director AS d LEFT JOIN pages_movie AS m ON d.name = m.director_id \
        LEFT JOIN pages_actor AS a ON a.name = m.actor_id \
        WHERE m.title LIKE %s", [tep])

    limit_tuple = filter_data[:1]
    for movie in limit_tuple:
        title = movie.title
        rating = movie.rating
        votes = movie.votes
        metascore = movie.metascore
        gross = movie.gross
        d_award = movie.d_win + movie.d_nom
        a_award = movie.a_win + movie.a_nom

    d_win_max = Director.objects.all().aggregate(r1=Max('award_win'))
    d_win_min = Director.objects.all().aggregate(r2=Min('award_win'))
    d_nom_max = Director.objects.all().aggregate(r3=Max('award_nom'))
    d_nom_min = Director.objects.all().aggregate(r4=Min('award_nom'))

    d_range = d_win_max.get('r1')+d_nom_max.get('r3') - \
        d_win_min.get('r2')-d_nom_min.get('r4')
    new_d_award = (d_award-(d_win_min.get('r2') -
                   d_nom_min.get('r4')))/d_range*100

    a_win_max = Actor.objects.all().aggregate(r1=Max('award_win'))
    a_win_min = Actor.objects.all().aggregate(r2=Min('award_win'))
    a_nom_max = Actor.objects.all().aggregate(r3=Max('award_nom'))
    a_nom_min = Actor.objects.all().aggregate(r4=Min('award_nom'))

    a_range = a_win_max.get('r1')+a_nom_max.get('r3') - \
        a_win_min.get('r2')-a_nom_min.get('r4')
    new_a_award = (a_award-(a_win_min.get('r2') -
                   a_nom_min.get('r4')))/a_range*100

    rating_max = Movie.objects.all().aggregate(rm1=Max('rating'))
    rating_min = Movie.objects.all().aggregate(rm2=Min('rating'))
    rating_range = rating_max.get('rm1')-rating_min.get('rm2')
    new_rating = (rating-rating_min.get('rm2'))/rating_range*100

    votes_max = Movie.objects.all().aggregate(rm1=Max('votes'))
    votes_min = Movie.objects.all().aggregate(rm2=Min('votes'))
    votes_range = votes_max.get('rm1')-votes_min.get('rm2')
    new_votes = (votes-votes_min.get('rm2'))/votes_range*100

    metascore_max = Movie.objects.all().aggregate(rm1=Max('metascore'))
    metascore_min = Movie.objects.all().aggregate(rm2=Min('metascore'))
    metascore_range = metascore_max.get('rm1')-metascore_min.get('rm2')
    new_metascore = (metascore-metascore_min.get('rm2'))/metascore_range*100

    gross_max = Movie.objects.all().aggregate(rm1=Max('gross_earning_in_mil'))
    gross_min = Movie.objects.all().aggregate(rm2=Min('gross_earning_in_mil'))
    gross_range = gross_max.get('rm1')-gross_min.get('rm2')
    new_gross = (gross-gross_min.get('rm2'))/gross_range*100

    context = {
        'filter_title': filter_title,
        'limit_tuple': limit_tuple,
        'new_rating': new_rating,
        'new_votes': new_votes,
        'new_d_award': new_d_award,
        'new_a_award': new_a_award,
        'ew_metascoren': new_metascore,
        'new_gross': new_gross
    }
    return render(request, template, context)


# def detail(request, id=None):
#     movie= get_object_or_404(Movie, id=id)
#     # items = []
#     # try:
#     #     if model.get_name() == 'movie' and id != 'None':
#     #         label = 'actor'
#     #         object = model.objects.get(movieid=id)
#     #         records = Act.objects.filter(movieid_id=id)
#     #         if request.user.get_username() != '':
#     #             seen_list = [str(x).split('|')[1] for x in
#     #                          Seen.objects.filter(username=request.user.get_username())]
#     #             expect_list = [str(y).split('|')[1] for y in
#     #                            Expect.objects.filter(username=request.user.get_username())]
#     #             if id in seen_list:
#     #                 object.flag = 1
#     #             if id in expect_list:
#     #                 object.flag = 2
#     #         for query in records:
#     #             for actor in Actor.objects.filter(actorid=query.actorid_id):
#     #                 items.append(actor)
#     #     if model.get_name() == 'actor':
#     #         label = 'movie'
#     #         object = model.objects.get(actorid=id)
#     #         records = Act.objects.filter(actorid_id=id)
#     #         for query in records:
#     #             for movie in Movie.objects.filter(movieid=query.movieid_id):
#     #                 items.append(movie)
#     # except:
#     #     return render(request, '404.html')
#     # return render(request, '{}_list.html'.format(label), {'items': items, 'number': len(items), 'object': object})
#     return render(request, 'movie_list.html', {'movie': movie,})
