from django.contrib import admin
from.models import *
# Register your models here.



admin.site.register(Plants)
admin.site.register(Pots)
admin.site.register(Pebbles)
admin.site.register(Fertilisers)
admin.site.register(Seeds)

admin.site.register(Plants_Products)
admin.site.register(Pebbles_Products)
admin.site.register(Pots_Products)
admin.site.register(Fertilisers_Products)
admin.site.register(Seeds_Products)