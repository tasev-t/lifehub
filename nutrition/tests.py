# nutrition/tests.py

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.utils import timezone
from django.contrib.auth import get_user_model
from nutrition.models import Recipe, Ingredient, MealPlan

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    """
    Vytvoří testovacího uživatele pro přístup k chráněným endpointům.
    """
    return User.objects.create_user(
        username='nutriuser',
        email='nutri@example.com',
        password='NutriPass123!'
    )

@pytest.fixture
def auth_client(api_client, test_user):
    """
    APIClient s JWT access tokenem v hlavičce.
    """
    resp = api_client.post(
        reverse('token_obtain_pair'),
        {'username': 'nutriuser', 'password': 'NutriPass123!'},
        format='json'
    )
    token = resp.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api_client

@pytest.mark.django_db
def test_ingredient_crud(auth_client):
    # Vytvoření ingredience
    create_resp = auth_client.post(
        reverse('ingredient-list'),
        {'name': 'Sugar', 'unit': 'g', 'quantity': 100},
        format='json'
    )
    assert create_resp.status_code == status.HTTP_201_CREATED
    ing_id = create_resp.data['id']

    # Výpis ingrediencí
    list_resp = auth_client.get(reverse('ingredient-list'))
    assert list_resp.status_code == status.HTTP_200_OK
    assert any(i['id'] == ing_id for i in list_resp.data)

    # Detail ingredience
    detail_resp = auth_client.get(reverse('ingredient-detail', args=[ing_id]))
    assert detail_resp.status_code == status.HTTP_200_OK
    assert detail_resp.data['name'] == 'Sugar'

    # Úprava ingredience
    update_resp = auth_client.put(
        reverse('ingredient-detail', args=[ing_id]),
        {'name': 'Brown Sugar', 'unit': 'g', 'quantity': 150},
        format='json'
    )
    assert update_resp.status_code == status.HTTP_200_OK
    assert update_resp.data['name'] == 'Brown Sugar'

    # Smazání ingredience
    del_resp = auth_client.delete(reverse('ingredient-detail', args=[ing_id]))
    assert del_resp.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_mealplan_crud(auth_client):
    # Vytvoření receptu
    recipe = Recipe.objects.create(
        title='Pancakes',
        description='Test pancakes',
        instructions='Mix and fry'
    )

    # Vytvoření jídelníčku
    today = timezone.now().date()
    mp_data = {
        'name': 'Breakfast Plan',
        'date': today.isoformat(),
        'recipes': [recipe.id]
    }
    create_resp = auth_client.post(reverse('mealplan-list'), mp_data, format='json')
    assert create_resp.status_code == status.HTTP_201_CREATED
    mp_id = create_resp.data['id']

    # Výpis jídelníčků
    list_resp = auth_client.get(reverse('mealplan-list'))
    assert list_resp.status_code == status.HTTP_200_OK
    assert any(m['id'] == mp_id for m in list_resp.data)

    # Detail jídelníčku
    detail_resp = auth_client.get(reverse('mealplan-detail', args=[mp_id]))
    assert detail_resp.status_code == status.HTTP_200_OK
    assert detail_resp.data['name'] == 'Breakfast Plan'
    assert recipe.id in detail_resp.data['recipes']

    # Úprava jídelníčku
    new_date = (today.replace(day=today.day + 1)).isoformat()
    upd_data = {
        'name': 'Brunch Plan',
        'date': new_date,
        'recipes': [recipe.id]
    }
    update_resp = auth_client.put(reverse('mealplan-detail', args=[mp_id]), upd_data, format='json')
    assert update_resp.status_code == status.HTTP_200_OK
    assert update_resp.data['name'] == 'Brunch Plan'

    # Smazání jídelníčku
    del_resp = auth_client.delete(reverse('mealplan-detail', args=[mp_id]))
    assert del_resp.status_code == status.HTTP_204_NO_CONTENT
