from rest_framework import viewsets

from car_dealership.api.v1.serializers.category_seriaizer import CategorySerializer
from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from car_dealership.models import  Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    pagination_class = APIListPagination
    search_fields = ['title']
