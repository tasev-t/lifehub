from rest_framework import serializers
from .models import Recipe, Ingredient, MealPlan

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit', 'quantity']

class MealPlanSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Recipe.objects.all()
    )
    class Meta:
        model = MealPlan
        fields = ['id', 'name', 'date', 'recipes']
