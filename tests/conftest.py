import pytest
from rest_framework.test import APIClient
from faker import Faker

@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def faker() -> Faker:
    return Faker()

