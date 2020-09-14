from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    bio = models.TextField()
    author_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    favorites = models.ManyToManyField('Recipe', blank=True, related_name='favorites')
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=40)
    instructions = models.TextField()