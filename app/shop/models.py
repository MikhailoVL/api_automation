from django.db import models

import datetime


class Product(models.Model):
    """Product model"""
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0, null=False)
    date_product = models.DateField(
        default=datetime.date.today().strftime('%Y-%m-%d'), blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    """Order model"""
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    date_order = models.DateField(
        default=datetime.date.today().strftime('%Y-%m-%d'), blank=True)
    is_payment = models.BooleanField(default=False)
    discount = models.IntegerField(default=0, null=True)

    def save(self, *args, **kwargs):
        if not self.discount:
            self.discount = self.set_discount()
        super(Order, self).save(*args, **kwargs)

    def set_discount(self):
        """checking if date create product more then 29 days
        set discount 20%
        """
        total = (datetime.date.today() - self.product.date_product).days
        if total > 30:
            return 20
        return 0

    def __str__(self):
        return str(self.product.title)


class Score(models.Model):
    """Score model"""
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    date_score = models.DateField(
        default=datetime.date.today().strftime('%Y-%m-%d'), blank=True)

    def __str__(self):
        return f' score #{self.id} order #' \
               f' {self.order.id} product title - {self.order.product.title}'
