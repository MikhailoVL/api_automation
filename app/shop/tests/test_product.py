from django.test import TestCase
import datetime

from shop import models


class ModelTest(TestCase):

    def test_create_product(self):
        """Test create product"""
        product = models.Product.objects.create(
            title="Book",
            price=14,
            date_product=datetime.date.today(),
        )
        self.assertEqual(product.title, "Book")

    def test_order_str(self):
        """Test the order string representation"""
        product = models.Product.objects.create(
            title="Book",
            price=14,
            date_product=datetime.date.today(),
        )
        order = models.Order.objects.create(
            product=product,
            status=False,
            date_order=datetime.date.today(),
            is_payment=False,
            discount=0
        )
        self.assertEqual(str(order), "Book")

    def test_create_score(self):
        """Test create score"""
        product = models.Product.objects.create(
            title="Book",
            price=14,
            date_product=datetime.date.today(),
        )
        order = models.Order.objects.create(
            product=product,
            status=False,
            date_order=datetime.date.today(),
            is_payment=False,
            discount=0
        )
        score = models.Score.objects.create(
            order=order,
            date_score=datetime.date.today()
        )

        self.assertEqual(models.Score, type(score))
