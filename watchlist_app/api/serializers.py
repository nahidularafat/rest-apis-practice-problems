from rest_framework import serializers
from watchlist_app import models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movielist
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviews
        fields = '__all__'     