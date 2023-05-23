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


class ArticleManager(models.Manager):
    def actual_articles(self):
        return self.filter(published_at__isnull=True).order_by("-created_at")


class Article(models.Model):
    objects = ArticleManager()

    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    highlight = models.BooleanField(default=False)
    picture = models.ImageField(
        upload_to="media/article_pictures", default="media/article_pictures/unicorn.jpg"
    )

    def __str__(self) -> str:
        return self.title
