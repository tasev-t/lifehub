from django.urls import path
from .views import (
    RecipeListCreateView, RecipeDetailView,
    IngredientListCreateView, IngredientDetailView,
    MealPlanListCreateView, MealPlanDetailView,
)

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient-detail'),
    path('mealplans/', MealPlanListCreateView.as_view(), name='mealplan-list'),
    path('mealplans/<int:pk>/', MealPlanDetailView.as_view(), name='mealplan-detail'),
]
