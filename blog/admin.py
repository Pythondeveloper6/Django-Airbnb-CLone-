from django.contrib import admin

# Register your models here.
from .models import Post , Category

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'



admin.site.register(Post , PostAdmin)
admin.site.register(Category)