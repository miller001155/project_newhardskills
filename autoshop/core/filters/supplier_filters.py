from django_filters import rest_framework as filters

import supplier
from supplier.models import Founder, Supplier


class SupplierFilter(filters.FilterSet):
    name = filters.CharFilter()
    class Meta:
        model = Supplier
        fields = ['name', 'location']


class FounderFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    company = filters.CharFilter()

    class Meta:
        model = Founder
        fields = ['first_name', 'company']