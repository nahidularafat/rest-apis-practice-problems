
from django.urls import  path

from watchlist_app import views
from watchlist_app.api import views
urlpatterns = [
    
    
    path('',views.MovieCreateView.as_view(),name='movie-list'),
    path('detail/<int:pk>/',views.MovieDetailView.as_view(),name='movie-detail')
]


