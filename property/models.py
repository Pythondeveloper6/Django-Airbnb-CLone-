from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Property(models.Model):
    owner = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=12000)
    price = models.IntegerField()
    place = models.CharField(max_length=50)
    image = models.ImageField(upload_to='propery/')
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Properties'

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Property, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property:property_detail' , kwargs={'slug':self.slug})



class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.property.title


    class Meta:
        verbose_name = 'Property Image'




class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name





class PropertyReview(models.Model):
    property = models.ForeignKey(Property, related_name='property_review', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='review_owner', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0 ,  validators=[MaxValueValidator(5)])
    feedback = models.TextField(default='' , max_length=200)


    def __str__(self):
        return self.property.title



PEOPLE_TYPE = (
    (1,1),
    (2,2),
    (3,3),
    (4,4)
)



class PropertyBook(models.Model):
    property = models.ForeignKey(Property, related_name='property_book', on_delete=models.CASCADE)
    name = models.CharField(max_length=50) 
    email = models.EmailField( max_length=254)
    date_from = models.DateField(default=timezone.now)
    date_to =  models.DateField(default=timezone.now)
    guest = models.IntegerField(default=1 , choices=PEOPLE_TYPE)
    children = models.IntegerField(default=0 , choices=PEOPLE_TYPE)


    def __str__(self):
        return self.property.title