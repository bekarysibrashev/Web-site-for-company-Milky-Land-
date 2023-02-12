from django.contrib import admin
from .models import Categories, News, Products, Info, Carusel, ImagesOfCarusel


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    


admin.site.register(Categories,MyModelAdmin)
admin.site.register(Products,MyModelAdmin)
admin.site.register(Info)
admin.site.register(Carusel)
admin.site.register(ImagesOfCarusel)
admin.site.register(News)
# Register your models here.
