from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
