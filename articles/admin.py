from django.contrib import admin
from articles.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'author', )
    search_fields = ('name', )
    list_filter = ('name',)
