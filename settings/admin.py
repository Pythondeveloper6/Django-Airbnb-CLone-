from django.contrib import admin

# Register your models here.
from . import models 




admin.site.register(models.About)
admin.site.register(models.Info)
admin.site.register(models.FAQ)