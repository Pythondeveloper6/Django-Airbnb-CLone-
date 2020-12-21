from django.contrib import admin

# Register your models here.
from .models import Property , PropertyImages , PropertyReview , Category , PropertyBook , Place
from django_summernote.admin import SummernoteModelAdmin
from tof.admin import TofAdmin, TranslationTabularInline

class PropertyAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

    list_display= ['title' , 'check_avablity' , 'get_avg_rating']


admin.site.register(Property,PropertyAdmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)


class CategoryAdmin(TofAdmin):
    list_display = ('id', 'name')
    inlines = (TranslationTabularInline, )

admin.site.register(Category , CategoryAdmin)


class RoomBookAdmin(admin.ModelAdmin):
    list_display = ('property','in_progress')



admin.site.register(PropertyBook , RoomBookAdmin)
admin.site.register(Place)