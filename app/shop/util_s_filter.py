from django_filters import rest_framework as filters

from .models import Order


class DateRangeFilter(filters.FilterSet):

    date_order = filters.DateFromToRangeFilter(
            label='Date (Between)', help_text="set date yyyy/mm/dd/")

    class Meta:
        model = Order
        # field_name = "date"
        fields = ['date_order']
