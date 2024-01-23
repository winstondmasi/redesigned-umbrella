from django.contrib import admin
from .models import Article, ArticleAnalysis

# registering models from models.py here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('url', 'submitted_on')
    search_fields = ('url',)
    list_filter = ('submitted_on',)

@admin.register(ArticleAnalysis)
class ArticleAnalysisAdmin(admin.ModelAdmin):
    list_display = ('article', 'bias_score', 'accuracy_score', 'analysis_date')
    search_fields = ('article__url',)
    list_filter = ('analysis_date', 'bias_score', 'accuracy_score')
