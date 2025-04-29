# users/tests.py

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    """
    APIClient bez přihlášení pro veřejné endpointy (registrace, token obtain).
    """
    return APIClient()

@pytest.fixture
def user_data():
    """
    Výchozí data pro registraci testovacího uživatele.
    """
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "StrongPass123!",
        "profile_mode": "personal"
    }

@pytest.mark.django_db
def test_registration_returns_201_and_user(api_client, user_data):
    """
    Testuje, že POST /api/users/register/ vrátí 201 a skutečně vytvoří uživatele.
    """
    url = reverse("user-register")
    resp = api_client.post(url, {
        "username": user_data["username"],
        "email": user_data["email"],
        "password": user_data["password"],
        "profile_mode": user_data["profile_mode"]
    }, format="json")
    assert resp.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username="testuser").exists()
    data = resp.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["profile_mode"] == "personal"

@pytest.mark.django_db
def test_token_obtain_and_refresh(api_client, user_data):
    """
    Testuje získání access/refresh tokenů a obnovu access tokenu.
    """
    # Nejprve registrace uživatele
    api_client.post(reverse("user-register"), {
        "username": user_data["username"],
        "email": user_data["email"],
        "password": user_data["password"],
        "profile_mode": user_data["profile_mode"]
    }, format="json")

    # Získání tokenů (obtain)
    token_url = reverse("token_obtain_pair")
    resp = api_client.post(token_url, {
        "username": user_data["username"],
        "password": user_data["password"]
    }, format="json")
    assert resp.status_code == status.HTTP_200_OK
    assert "access" in resp.data and "refresh" in resp.data

    # Obnovení access tokenu (refresh)
    refresh = resp.data["refresh"]
    refresh_url = reverse("token_refresh")
    resp2 = api_client.post(refresh_url, {"refresh": refresh}, format="json")
    assert resp2.status_code == status.HTTP_200_OK
    assert "access" in resp2.data

@pytest.fixture
def auth_client(api_client, user_data):
    """
    APIClient s již nastaveným Authorization header (JWT access).
    """
    api_client.post(reverse("user-register"), {
        "username": user_data["username"],
        "email": user_data["email"],
        "password": user_data["password"],
        "profile_mode": user_data["profile_mode"]
    }, format="json")
    token = api_client.post(reverse("token_obtain_pair"), {
        "username": user_data["username"],
        "password": user_data["password"]
    }, format="json").data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client

@pytest.mark.django_db
def test_get_profile(auth_client):
    """
    Testuje GET /api/users/profile/ pro přihlášeného uživatele.
    """
    resp = auth_client.get(reverse("user-profile"))
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data["username"] == "testuser"
    assert resp.data["profile_mode"] in ["personal", "family"]

@pytest.mark.django_db
def test_put_profile_change_to_family(auth_client):
    """
    Testuje PUT /api/users/profile/ změnu módu na 'family' včetně vytvoření FamilyGroup.
    """
    resp = auth_client.put(reverse("user-profile"), {"profile_mode": "family"}, format="json")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data["profile_mode"] == "family"
    assert resp.data.get("family_group") is not None

@pytest.mark.django_db
def test_put_profile_invalid_mode(auth_client):
    """
    Testuje, že neplatný mód vrátí HTTP 400 Bad Request.
    """
    resp = auth_client.put(reverse("user-profile"), {"profile_mode": "foo"}, format="json")
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
