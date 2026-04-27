from django.contrib import admin
from apps.home.models import*
from django.db.models import Count
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'chapter', 'created_at', 'slug', 'is_feature', 'is_highlighted']
    prepopulated_fields = { 'slug': ('title',), }
    list_filter = ['created_at', 'is_feature', 'is_highlighted', 'chapter']
    search_fields = ['title', 'body']
    list_per_page = 6

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'date_updated']
    prepopulated_fields = { 'slug': ('title',), }
    list_per_page = 6

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'article', 'image', 'created_at']
    search_fields = ['article__title',]
    list_filter = [ 'chapter', 'created_at' ] #, 


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at']
    list_filter = [ 'created_at' ] #, 




@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'department_count']
    readonly_fields = ['department_count']
    prepopulated_fields = { 'slug': ('name',)} 

    def department_count(self, obj):
        return obj.departments.count()
    department_count.short_description = 'Department Count'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['faculty','name', ]
    list_filter = [ 'faculty' ] #, 


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty','year_launched', 'slug']
    list_filter = [ 'faculty' ] #,
    prepopulated_fields = { 'slug': ('name',)} 



@admin.register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'rank', 'first_name', 'middle_name', 'surname' ]

@admin.register(Secretariat)
class SecretariatAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'first_name', 'middle_name', 'surname' ]

