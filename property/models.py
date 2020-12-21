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
    place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
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


    def check_avablity(self):
        all_reservations = self.property_book.all()
        now = timezone.now().date()
        for reservation in all_reservations:
            if now > reservation.date_to : 
                return 'Avialable'

            elif now > reservation.date_from and now < reservation.date_to:
                reserved_to = reservation.date_to
                return f'In Progress to {reserved_to}'
        else:
            return 'Avialable'


    def get_avg_rating(self):
        all_reviews = self.property_review.all()
        all_ratings = 0
    
        if len(all_reviews) > 0 : 
            for review in all_reviews:
                all_ratings += review.rating
            
            return round(all_ratings / len(all_reviews) , 2)
        else:
            return '-'



class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='places/')

    class Meta:
        verbose_name = ("Place")
        verbose_name_plural = ("Places")

    def __str__(self):
        return self.name






class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.property.title


    class Meta:
        verbose_name = 'Property Image'




class Category(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=25 , blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name.en





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
    name = models.ForeignKey(User, related_name='user_book', on_delete=models.CASCADE) 
    date_from = models.DateField(default=timezone.now)
    date_to =  models.DateField(default=timezone.now)
    guest = models.IntegerField(default=1 , choices=PEOPLE_TYPE)
    children = models.IntegerField(default=0 , choices=PEOPLE_TYPE)


    def __str__(self):
        return self.property.title



    def in_progress(self):
        now = timezone.now().date()
        return now > self.date_from and now < self.date_to

    in_progress.boolean = True
