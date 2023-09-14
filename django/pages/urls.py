from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('movie/', views.movie, name = 'movie'),
    path('director/', views.director, name = 'director'),
    path('actor/', views.actor, name = 'actor'),
    path('movies/', views.MovieAPI.as_view(), name = 'movie-api'),
    path('directors/', views.DirectorAPI.as_view(), name = 'director-api'),
    path('actors/', views.ActorAPI.as_view(), name = 'actor-api'),
    path('actors/<str:id>/films/', views.ActorFilmsAPI.as_view(), name = 'actor_films'),
    path('directors/<str:id>/films/', views.DirectorFilmsAPI.as_view(), name = 'director_films'),
    path('movies/best/<int:count>', views.BestMoviesAPI.as_view(), name = 'best_movie_with_count'),
    path('movies/best/', views.BestMoviesAPI.as_view(), name = 'best_movie'),
    path('actors/birthdays/<str:date>/', views.ClosetToActorBirthday.as_view(), name='closet-to-actors-birthday'),
    path('recommendation/', views.recommendation, name = 'recommendation'),
    path('insert_data/', views.insert_data, name = 'insert_data'),
    path('insert_data_submission/', views.insert_data_submission, name = 'insert_data_submission'),
    path('new_movie/', views.new_movie, name='new_movie'),
    re_path(r'^edit_movie/(?P<pk>\d+)/$', views.edit_movie, name='edit_movie'),
    re_path(r'^delete_movie/(?P<pk>\d+)/$', views.delete_movie, name='delete_movie'),
]

