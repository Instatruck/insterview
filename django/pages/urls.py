from django.urls import path
from django.conf.urls import url
from . import views
from pages.api_views import (
    MovieListView, ActorListView, DirectorListView, ActorFilmsView, DirectorFilmsView
)
urlpatterns = [
    path('', views.home, name='home'),
    path('movie/', views.movie, name='movie'),
    path('director/', views.director, name='director'),
    path('actor/', views.actor, name='actor'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('insert_data/', views.insert_data, name='insert_data'),
    path('insert_data_submission/', views.insert_data_submission, name='insert_data_submission'),
    path('new_movie/', views.new_movie, name='new_movie'),
    url(r'^edit_movie/(?P<pk>\d+)/$', views.edit_movie, name='edit_movie'),
    url(r'^delete_movie/(?P<pk>\d+)/$', views.delete_movie, name='delete_movie'),
    # New API Endpoints
    path('api/movies/', MovieListView.as_view(), name='api_movies_list'),
    path('api/actors/', ActorListView.as_view(), name='api_actors_list'),
    path('api/directors/', DirectorListView.as_view(), name='api_directos_list'),
    path('api/actors/<str:name>/films/', ActorFilmsView.as_view(), name='actor_films'),
    path('api/directors/<str:name>/films/', DirectorFilmsView.as_view(), name='director_films'),
    
]
