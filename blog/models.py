from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})



class Category(models.Model):
    name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

