#-------------------------------------------------#
# Title: admin.py
# Dev:   Scott Luse
# Changelog:
# Aug 11, 2018: Django REST framework
#-------------------------------------------------#

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    # posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='posts')

    def __str__(self):
        return self.title
