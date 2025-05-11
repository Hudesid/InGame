from django.contrib import admin
from .models import Game, Fps


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'game_name')
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(Fps)
class FpsAdmin(admin.ModelAdmin):
    list_display = ('id', 'desktop', 'game_fps', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'desktop', 'game')
    search_fields = ('id', 'game_fps')
    readonly_fields = ('id', 'created_at', 'updated_at')
