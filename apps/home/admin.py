from django.contrib import admin
from apps.home.models import*
from django.db.models import Count
# Register your models here.

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'chapter', 'created_at', 'slug', 'is_feature', 'is_highlighted']
#     prepopulated_fields = { 'slug': ('title',), }
#     list_filter = ['created_at', 'is_feature', 'is_highlighted', 'chapter']
#     search_fields = ['title', 'body']
#     list_per_page = 6


@admin.register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'rank', 'first_name', 'middle_name', 'surname' ]

@admin.register(Secretariat)
class SecretariatAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'first_name', 'middle_name', 'surname' ]

