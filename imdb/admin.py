from django.contrib import admin

# Register your models here.
from imdb.models import Rating,Movie,Cast,Actor,Director

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Rating)
admin.site.register(Director)

