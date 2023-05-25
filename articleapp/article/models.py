from django.db import models
from django.db.models.fields import CharField, TextField, DateTimeField, BooleanField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.


class Tag(models.Model):
    name: CharField = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name: CharField = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class ArticleManager(models.Manager):
    def actual_articles(self):
        return self.filter().order_by("-created_at")


class Article(models.Model):
    objects: ArticleManager = ArticleManager()

    title: CharField = models.CharField(max_length=250)
    perex: TextField = models.TextField()
    content: TextField = models.TextField()
    author: ForeignKey = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tag: ManyToManyField = models.ManyToManyField(Tag)
    category: ForeignKey = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_at: DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: DateTimeField = models.DateTimeField(auto_now=True)
    published_at: DateTimeField = models.DateTimeField(null=True, blank=True)
    highlight: BooleanField = models.BooleanField(default=False)
    picture: ImageField = models.ImageField(
        upload_to="media/article_pictures", default="media/article_pictures/unicorn.jpg"
    )

    def __str__(self) -> str:
        return self.title
