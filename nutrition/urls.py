from django.urls import path
from .views import (
    RecipeListView,
    IngredientListCreateView, IngredientDetailView,
    MealPlanListCreateView, MealPlanDetailView,
)

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient-detail'),
    path('mealplans/', MealPlanListCreateView.as_view(), name='mealplan-list'),
    path('mealplans/<int:pk>/', MealPlanDetailView.as_view(), name='mealplan-detail'),
]
