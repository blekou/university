from django.db import models

# Create your models here.

class CategorieArticle(models.Model):

    nom = models.CharField(max_length=225)
    image= models.ImageField()
    description = models.TextField()

    date_add =models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=True)

    class Meta:
        verbose_name = 'categories article'
        verbose_name_plural = 'categories articles'

    def __str__(self):
        return self.nom + self.image


class Tag(models.Model):

    nom = models.CharField(max_length=225)
    description = models.TextField()

    date_add =models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.nom


class Article(models.Model):

    titre = models.CharField(max_length=225)
    image= models.ImageField()
    description = models.TextField()
    contenu= models.TextField()
    categorie=models.ForeignKey(CategorieArticle, on_delete=models.CASCADE, related_name='categorie_Article')
    tag =models.ManyToManyField(Tag, related_name='tag_article')

    date_add =models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = ' articles'

    def __str__(self):
        return self.titre + self.description



class Commentaire(models.Model):

    nom = models.CharField(max_length=225)
    prenom= models.CharField(max_length=225)
    article = models.ForeignKey(Article, related_name='commentaire_ariticle', on_delete=models.CASCADE)
    commentaire =models.TextField()
    date_add =models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=True)

    class Meta:
        verbose_name = 'commentaire'
        verbose_name_plural = ' commentaires'

    def __str__(self):
        return self.nom + self.commentaire





