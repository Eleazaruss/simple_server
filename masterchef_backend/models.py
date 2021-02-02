from django.db import models
from jsonfield import JSONField

class Recipe(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=300)
    ingredients = JSONField(default=list, null=True, blank=True)
    steps = models.TextField(max_length=1000)
    time = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=32)
    isFavorite = models.BooleanField()

    def __str__(self):
        return self.name