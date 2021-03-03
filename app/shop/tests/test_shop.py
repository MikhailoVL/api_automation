from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import Group

from shop import models

ORDERS_URL = reverse('orders')


def sample_user_with_set_group(email='test_user@gmail.com', password='test12'):
    """Create a sample user and set hem in to group"""
    user = get_user_model().objects.create_user(email, password)
    Group.objects.get_or_create(name='Booker')
    group = Group.objects.get(name='Booker')
    group.user_set.add(user)

    return user


class ModelTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login required to access the endpoint"""
        res = self.client.get(ORDERS_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_with_required(self):
        """Test that checking the access of a user who has an access group"""
        user = sample_user_with_set_group()
        self.client.login(username='test_user@gmail.com', password='test12')
        res = self.client.get(ORDERS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
