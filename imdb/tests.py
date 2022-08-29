from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
import pytest

@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='me')
    assert me.is_superuser