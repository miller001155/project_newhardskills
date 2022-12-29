from rest_framework import viewsets

from purchaser.api.v1.serializers.purchaser_serializer import PurchaserSerializer
from purchaser.api.v1.views.balance_view import APIListPaginationPurchaser
from purchaser.models import  Purchaser



class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all().order_by('first_name')
    serializer_class = PurchaserSerializer
    pagination_class = APIListPaginationPurchaser
