from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from pages.models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer


class MovieListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def filter_queryset(self, queryset):
        params = self.request.query_params
        
        # Implement date-filtering
        start_year = params.get('start_year')
        end_year = params.get('end_year')
        if start_year:
            queryset = queryset.filter(year__gte=start_year)
        if end_year:
            queryset = queryset.filter(year__lte=end_year)

        return queryset

    
class Top10MovieListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.order_by('-rating', '-metascore')[:10]


class TopMovieListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer

    def get_queryset(self):
        n = self.kwargs['n']
        return Movie.objects.order_by('-rating', '-metascore')[:n]


class ActorListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class ActorFilmsListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer

    def get_queryset(self):
        actor = Actor.objects.get(pk=self.kwargs['pk'])
        return Movie.objects.filter(actor=actor)


class ActorNearestToBirthdayListView(ListAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        date = kwargs['date']
        try:
            date = datetime.strptime(date, "%d%m%Y").date().replace(year=2000)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        actors = list(Actor.objects.all())
        actors.sort(
            key=lambda actor:
                abs((datetime.strptime(actor.date, "%d%m%Y").date().replace(year=2000) - date).days)
        )

        return Response(ActorSerializer(actors, many=True).data)



class DirectorListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()


class DirectorFilmsListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer

    def get_queryset(self):
        director = Director.objects.get(pk=self.kwargs['pk'])
        return Movie.objects.filter(director=director)
