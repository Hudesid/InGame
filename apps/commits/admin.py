from django.contrib import admin
from .models import Comment, DesktopComment, ProductComment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'username')
    search_fields = ('id', 'comment_uz', 'comment_ru', 'description_uz', 'description_uz')
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(DesktopComment)
class DesktopCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'rating', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'username', 'rating', 'desktop')
    search_fields = ('id', 'comment')
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'rating', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'username', 'rating', 'product')
    search_fields = ('id', 'comment')
    readonly_fields = ('id', 'created_at', 'updated_at')