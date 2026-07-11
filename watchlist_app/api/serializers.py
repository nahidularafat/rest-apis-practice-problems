from rest_framework import serializers
from watchlist_app import models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movielist
        fields = '__all__'
     