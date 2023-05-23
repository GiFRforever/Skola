from django.shortcuts import render
from django.views.generic import TemplateView
from article.models import Article
import random


class HomePageView(TemplateView):
    template_name = "article/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # article = Article.objects.first()
        actual_articles = Article.objects.actual_articles()
        context.update(
            {
                "actual_articles": actual_articles,
                "title": "Homepage",
                "random_number": random.randint(1, 100),
            }
        )
        return context


class AboutPageView(TemplateView):
    template_name = "article/about.html"
