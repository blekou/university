from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Infosite),
admin.site.register(models.CompteSocial),
admin.site.register(models.Presentation),
admin.site.register(models.Temoignage)