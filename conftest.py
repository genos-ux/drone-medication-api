import pytest
import django
from django.conf import settings

@pytest.fixture(scope='session', autouse=True)
def setup_django():
    django.setup()
