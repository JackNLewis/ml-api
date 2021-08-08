from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    description = models.TextField()
    content = models.TextField()
    image_dir = "images/milky-way.jpeg"
    image = models.ImageField(upload_to ='images/', default=image_dir)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title