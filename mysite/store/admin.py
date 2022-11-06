from django.contrib import admin
from .models import Phone,Variation,ReviewRating,ProductGallery,Brand

# Register your models here.

admin.site.register(Brand)
admin.site.register(Phone)
admin.site.register(Variation)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)