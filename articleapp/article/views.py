from django.shortcuts import render
from django.views.generic import TemplateView
from article.models import Article, ArticleManager
import random
from typing import Any


class HomePageView(TemplateView):
    template_name: str = "article/homepage.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        # article = Article.objects.first()
        actual_articles: ArticleManager = Article.objects.actual_articles()
        context.update(
            {
                "actual_articles": actual_articles,
                "title": "Homepage",
                "random_number": random.randint(1, 100),
            }
        )
        return context


class TeaPageView(TemplateView):
    template_name: str = "article/tea.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        # article = Article.objects.first()
        actual_articles: ArticleManager = Article.objects.actual_articles()
        context.update(
            {
                "actual_articles": actual_articles,
                "title": "Tea",
                # "random_number": random.randint(1, 100),
            }
        )
        return context


class DetailArticleView(TemplateView):
    template_name: str = "article/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        try:
            article = Article.objects.get(pk=kwargs.get("pk"))
        except Article.DoesNotExist:
            article = Article.objects.first()
        context.update(
            {
                "article": article,
            }
        )
        return context


class AboutPageView(TemplateView):
    template_name: str = "article/about.html"
