from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/'  , blank=True, null=True)
    phone_number = models.CharField(max_length=16 , blank=True, null=True)
    address = models.CharField(max_length=50 , blank=True, null=True)


    def __str__(self):
        return str(self.user)

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)