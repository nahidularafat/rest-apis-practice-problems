
from django.urls import  path

from watchlist_app import views
from watchlist_app.api import views
urlpatterns = [
    
    path('/',views.movie_list,name='movie-list'),
]
