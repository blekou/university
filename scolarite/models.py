from django.db import models

# Create your models here.

class Categorie(models.Model):

    nom = models.CharField(max_length=225)
    description= models.TextField()
    image =models.ImageField()

    date_add = models.DateTimeField(auto_now_add = True )
    date_update = models.DateTimeField(auto_now = True )
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = 'categorie de frais'
        verbose_name_plural = 'categorie de frais'


    def __str__(self):
        return self.nom


class Frais(models.Model):

    name = models.CharField(max_length=225)
    image = models.ImageField()
    description = models.TextField()
    prix = models.FloatField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie_frais')


    date_add = models.DateTimeField(auto_now_add = True )
    date_update = models.DateTimeField(auto_now = True )
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'frais'
        verbose_name_plural = 'frais'

    def __str__(self):
        return self.prix