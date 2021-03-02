from rest_framework.generics import ListAPIView, CreateAPIView,\
    UpdateAPIView, RetrieveAPIView
from .serializers import OrderSerializer, ScoreSerializer
from .models import Order, Score
from .permissions import HasGroupPermission
from .util_s_filter import DateRangeFilter
from django_filters import rest_framework as filters


class OrderListAPIView(ListAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Booker', 'Cashier', 'Sales_assistant'],
    }
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DateRangeFilter


class OrderCreateAPIView(CreateAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Cashier'],
        'POST': ['Cashier'],
        'PUT': ['Cashier'],

    }
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderUpdateAPIView(UpdateAPIView, RetrieveAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Cashier', 'Sales_assistant'],
        'POST': ['Cashier', 'Sales_assistant'],
        'PUT': ['Cashier', 'Sales_assistant'],

    }
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class ScoreCreateAPIView(CreateAPIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['Cashier'],
        'POST': ['Cashier'],
        'PUT': ['Cashier'],
    }
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
