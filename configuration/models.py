from django.db import models

# Create your models here.
class Infosite(models.Model):
    nom=models.CharField(max_length=225)
    mapurl=models.URLField()
    email = models.EmailField()
    logo=models.ImageField()

    class Meta:
        verbose_name ='info site'
        verbose_name_plural ='info sites'

    def __str__(self):
        return self.nom

class CompteSocial(models.Model):

    nom=models.CharField(max_length=225)
    liens=models.URLField()
    ICONE =[
        ('facebook', 'fab fa-facebook'),
        ('linkedin', 'fab fa-linkedin'),
        ('instagram', 'fab fa-instagram'),
        ('googleplus', 'fab fa-googleplus'),
    ]
    icones=models.ImageField(ICONE)
    logo=models.ImageField()

    class Meta:
        verbose_name ='compte social'
        verbose_name_plural ='compte socials'

    def __str__(self):
        return self.nom


class Presentation(models.Model):

    nom = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField()
    video=models.TextField()

    date_add =models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=True)

    class Meta:
        verbose_name ='presentation'
        verbose_name_plural ='presentation'

    def __str__(self):
        return self.nom

class Temoignage(models.Model):

    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    photo = models.ImageField()
    message=models.TextField()

    class Meta:
        verbose_name ='temoignage'
        verbose_name_plural ='temoignages'

    def __str__(self):
        return self.nom