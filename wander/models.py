from django.contrib.auth.models import AbstractUser
from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.


class Wanderer(AbstractUser):
    current_position = GeopositionField()
    # profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)


class Category(models.Model):
    name = models. CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Wanderer, related_name='categories')

    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models. CharField(max_length=50)
    streetnum = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    zipcode = models.IntegerField(max_length=10, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='locations')
    image = models.ImageField(upload_to='location_image', blank=True, null=True)

    def __unicode__(self):
        return self.name



