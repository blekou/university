from django.db import models

# Create your models here.
class Admission(models.Model):

    nom=models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    email = models.EmailField()
    message=models.TextField()
    numero =models.CharField(max_length=12)

    class Meta:
        verbose_name ='Admission'
        verbose_name_plural ='Admissions'

    def __str__(self):
        return self.nom

class Formation(models.Model):

    nom = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name ='Formation'
        verbose_name_plural ='Formation'

    def __str__(self):
        return self.nom





