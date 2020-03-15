from django.db import models

# Create your models here.
class Contact(models.Model):

    nom = models.CharField(max_length=225)
    email = models.EmailField()
    sujet = models.TextField()
    message = models.TextField

    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status =models.BooleanField(default= True)


    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.nom


class Newsletter(models.Model):

    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status =models.BooleanField(default= True)


    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'

    def __str__(self):
        return self.email