from django.db import models
from django.conf import settings

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructions = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # jednotka, např. g, ml, ks
    unit = models.CharField(max_length=20, blank=True)
    # množství pro základní recept (volitelné, viz další rozšíření)
    quantity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    # jídelníček obsahuje více receptů
    recipes = models.ManyToManyField(Recipe, related_name='mealplans')
    # nepovinně můžete přidat vztah k uživateli, pokud budete ukládat uživatelské plány:
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mealplans')

    def __str__(self):
        return f"{self.name} ({self.date})"
