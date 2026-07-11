
from django.urls import  path

from watchlist_app import views

urlpatterns = [
    
    path('/',views.movie_list,name='movie-list'),
]
