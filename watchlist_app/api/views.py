from watchlist_app import models
from . import serializers
from rest_framework.response import Response   
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# @api_view(['GET'])
# def movie_list(request):
#     movies = models.Movielist.objects.all()
#     serializer = serializers.MovieSerializer(movies, many=True)
#     return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_list(request):
   if request.method == 'GET':   
    movies = models.Movielist.objects.all()
    serializer = serializers.MovieSerializer(movies, many=True)
    return Response(serializer.data)
   elif request.method == 'POST':
     serializer = serializers.MovieSerializer(data=request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=201)
     return Response(serializer.errors, status=400)   
   
@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def movie_detail(request, pk):
  movie =get_object_or_404(models.Movielist, pk=pk)
  if request.method == 'GET':
    serializer = serializers.MovieSerializer(movie)
    return Response(serializer.data)   
  elif request.method == 'PUT':
    serializer = serializers.MovieSerializer(movie, data=request.data , partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=400)
  elif request.method == 'PATCH':
    serializer = serializers.MovieSerializer(movie, data=request.data , partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=400)
  elif request.method == 'DELETE':
    movie.delete()
    return Response(status=204)