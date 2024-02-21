from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view()),
    path('movies/best/', views.Top10MovieListView.as_view()),
    path('movies/best/<int:n>/', views.TopMovieListView.as_view()),
    path('actors/', views.ActorListView.as_view()),
    path('actors/<pk>/films/', views.ActorFilmsListView.as_view()),
    path('actors/birthdays/<date>/', views.ActorNearestToBirthdayListView.as_view()),
    path('directors/', views.DirectorListView.as_view()),
    path('directors/<pk>/films/', views.DirectorFilmsListView.as_view()),
]
