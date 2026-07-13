from pyclbr import Class

from django.db import models

# Create your models here.
class Movielist(models.Model) :
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
        # Git test


class Reviews(models.Model):
    movie = models.ForeignKey(Movielist, on_delete=models.CASCADE, related_name='reviews')
    review_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)