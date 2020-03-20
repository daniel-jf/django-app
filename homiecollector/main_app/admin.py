from django.contrib import admin
# Register your models here.
from .models import Homie, Saw, Location

admin.site.register(Homie)
admin.site.register(Saw)
admin.site.register(Location)