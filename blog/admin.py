from django.contrib import admin
from .models import Post, Comment, Category
from import_export.admin import ImportExportModelAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'help_img', 'author', 'category', 'post_date', 'post_update']
    search_fields = ['title', 'content', 'help_img', 'author', 'category', 'post_date', 'post_update']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'body', 'comment_date', 'active', 'post']
    search_fields = ['name', 'email', 'body', 'comment_date', 'active', 'post']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]