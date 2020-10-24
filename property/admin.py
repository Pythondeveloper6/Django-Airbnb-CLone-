from django.contrib import admin

# Register your models here.
from .models import Property , PropertyImages , PropertyReview , Category




admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)