import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client: APIClient):
    def do_authentication(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))

    return do_authentication
