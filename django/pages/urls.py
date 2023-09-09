from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('movies/', views.MovieAPI.as_view(), name = 'movie'),
    path('directors/', views.DirectorAPI.as_view(), name = 'director'),
    path('actors/', views.ActorAPI.as_view(), name = 'actor'),
    path('actors/<str:id>/films/', views.ActorFilmsAPI.as_view(), name = 'actor'),
    path('directors/<str:id>/films/', views.DirectorFilmsAPI.as_view(), name = 'actor'),
    path('recommendation/', views.recommendation, name = 'recommendation'),
    path('insert_data/', views.insert_data, name = 'insert_data'),
    path('insert_data_submission/', views.insert_data_submission, name = 'insert_data_submission'),
    path('new_movie/', views.new_movie, name='new_movie'),
    re_path(r'^edit_movie/(?P<pk>\d+)/$', views.edit_movie, name='edit_movie'),
    re_path(r'^delete_movie/(?P<pk>\d+)/$', views.delete_movie, name='delete_movie'),
]
