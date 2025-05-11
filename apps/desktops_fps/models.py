from django.db import models
from apps.desktops.models import Desktop


class Game(models.Model):
    game_name = models.CharField(max_length=255)
    game_image = models.ImageField(upload_to="desktops_fps_game_image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.game_name


class Fps(models.Model):
    game_fps = models.CharField(max_length=255)
    desktop = models.ForeignKey(Desktop, on_delete=models.CASCADE, related_name="fps")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="fps")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.game_fps