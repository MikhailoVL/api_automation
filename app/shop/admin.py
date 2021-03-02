from django.contrib import admin
from .models import Product, Order, Score


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount']


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(Score)
