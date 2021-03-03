from rest_framework import serializers

from .models import Order, Product, Score


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the product object"""
    title = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    date_product = serializers.DateField(required=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the order object

    override the create method and the to_representation
     method to change the behavior
      (creating an order via title for set in request title instead of pk)
    """

    product = serializers.PrimaryKeyRelatedField(
                                                queryset=Product.objects.all())
    price = serializers.SerializerMethodField(
                                method_name='calculate_price', read_only=True)

    def calculate_price(self, instance):
        product_price = instance.product.price
        discount = instance.discount
        return product_price - discount * (product_price / 100)

    class Meta:
        model = Order
        fields = ['id', 'product', 'status', 'date_order',
                  'is_payment', 'discount', 'price'
                  ]


class ScoreSerializer(serializers.ModelSerializer):
    """Serializer for the score object"""

    # add field to representation
    price_product = serializers.SerializerMethodField(
                                    method_name='get_price_product')
    title_product = serializers.SerializerMethodField(
                                    method_name='get_title_product')
    date_order = serializers.SerializerMethodField(
                                    method_name='get_date_order')

    def get_title_product(self, instance):
        return instance.order.product.title

    def get_price_product(self, instance):
        price = instance.order.product.price
        discount = instance.order.discount
        return price - discount * (price / 100)

    def get_date_order(self, instance):
        return instance.order.date_order

    class Meta:
        model = Score
        fields = ['order', 'title_product', 'price_product',
                  'date_score', 'date_order']
