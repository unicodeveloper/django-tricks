from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=200)
  slug = models.CharField(max_length=400)
  description = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

class Tag(models.Model):
  name = models.CharField(max_length=200)
  slug = models.CharField(max_length=400)
  user = models.ForeignKey('auth.User')
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)


class Profile(models.Model):
  user = models.ForeignKey('auth.User')
  username = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  location = models.CharField(max_length=200,null=True)
  description = models.TextField(null=True)
  image_url = models.TextField()
  access_token = models.TextField()
  access_token_secret = models.TextField()

class Trick(models.Model):
  title = models.CharField(max_length=200)
  slug  = models.CharField(max_length=400)
  description = models.CharField(max_length=700)
  code  = models.TextField()
  vote_cache = models.IntegerField(default=0)
  view_cache = models.IntegerField(default=0)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  user  = models.ForeignKey('auth.User')

class Vote(models.Model):
  user = models.ForeignKey('auth.User')
  trick = models.ForeignKey(Trick)

class Tag_Trick(models.Model):
  trick = models.ForeignKey(Trick)
  tag = models.ForeignKey(Tag)

class Category_Trick(models.Model):
  category = models.ForeignKey(Category)
  trick = models.ForeignKey(Trick)

