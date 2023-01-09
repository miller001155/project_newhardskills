from django_filters import rest_framework as filters

import supplier
from supplier.models import Founder


class SupplierFilter(filters.FilterSet):
    name = filters.CharFilter()
    location = filters.ChoiceFilter()
    class Meta:
        model = supplier
        fields = ['name', 'location']


class FounderFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    company = filters.CharFilter()

    class Meta:
        model = Founder
        fields = ['first_name', 'company']