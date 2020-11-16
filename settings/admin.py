from django.contrib import admin

# Register your models here.
from . import models 
from django_summernote.admin import SummernoteModelAdmin

class AboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(models.About , AboutAdmin)
admin.site.register(models.Info)
admin.site.register(models.FAQ)