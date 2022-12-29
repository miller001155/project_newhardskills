from rest_framework import viewsets

from supplier.api.v1.serializers.supplier_serializer import SupplierSerializer
from supplier.api.v1.views.founder_view import APIListPaginationFounder
from supplier.models import  Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer
    pagination_class = APIListPaginationFounder
