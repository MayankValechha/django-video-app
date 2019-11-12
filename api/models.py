from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# ModelResource class is used to create API by extending ModelResource class


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
