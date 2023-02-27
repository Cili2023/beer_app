from django.contrib import admin

from .models import Manufacturer, BeerType, Beer, Review

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(BeerType)
admin.site.register(Beer)
admin.site.register(Review)