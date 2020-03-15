from django.db import models

# Create your models here.
class Event(models.Model):

    nom = models.CharField(max_length=225),
    image =models.ImageField()
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add =True)
    date_update = models.DateTimeField(auto_now =True)
    status =models.BooleanField(default = True)

    class Meta:
        verbose_name='evenement'
        verbose_name_plural='evenements'

    def __str__(self):
        return  self.nom


class CategorieEvent(models.Model):

    nom = models.CharField(max_length = 225)
    categorie = models.ForeignKey(Event, on_delete =models.CASCADE, related_name= 'categorie_event')
    image = models.ImageField()
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add =True)
    date_update = models.DateTimeField(auto_now =True)
    status =models.BooleanField(default = True)

    class Meta:
        verbose_name = "categorie d'evenement "
        verbose_name_plural = "categorie d'evenements"

    def __str__(self):
        return self.nom