from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.filters.supplier_filters import SupplierFilter
from supplier.api.v1.serializers.supplier_serializer import SupplierSerializer
from supplier.api.v1.views.founder_view import APIListPaginationFounder
from supplier.models import  Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer
    pagination_class = APIListPaginationFounder
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    search_fields = ['name', 'location']
