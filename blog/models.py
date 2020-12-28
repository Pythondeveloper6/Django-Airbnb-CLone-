from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.CASCADE , verbose_name=_('author'))
    title = models.CharField(max_length=50 , verbose_name=_('title'))
    description = models.TextField(max_length=10000 , verbose_name=_('description'))
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(_('image') ,upload_to='blog/')
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE , verbose_name=_('category'))
    tags = TaggableManager(_('tags') ,blank=True)
    slug = models.SlugField(_('slug') ,blank=True, null=True)
    actvie = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)    
       super(Post, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})



class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(_('slug') ,blank=True, null=True)


    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)    
       super(Category, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


