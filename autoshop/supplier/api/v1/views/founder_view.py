from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from purchaser.api.v1.serializers.balance_serializer import BalanceSerializer
from supplier.models import  Founder



class APIListPaginationFounder(PageNumberPagination):
    page_size = 7
    page_query_param = 'page_side'
    max_page_size = 12
class FounderViewSet(viewsets.ModelViewSet):
    queryset = Founder.objects.all().order_by('first_name')
    serializer_class = BalanceSerializer
    pagination_class = APIListPaginationFounder
