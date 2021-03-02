from django.urls import path

from .api_views import OrderListAPIView, OrderCreateAPIView,\
    OrderUpdateAPIView, ScoreCreateAPIView

urlpatterns = [
    path('orders/', OrderListAPIView.as_view(), name='orders'),
    path('create_order/', OrderCreateAPIView.as_view(), name='create_order'),
    path('order_update/<int:pk>/', OrderUpdateAPIView.as_view(),
         name='order_update'),
    path('generate_score/', ScoreCreateAPIView.as_view(),
         name='generate_score'),
]
