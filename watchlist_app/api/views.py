from watchlist_app import models
from . import serializers
from rest_framework.response import Response   
from rest_framework.decorators import api_view

def movie_list(movielist):
    movies = models.Movielist.objects.all()
    serializer = serializers.MovieSerializer(movies, many=True)
    return Response(serializer.data)

