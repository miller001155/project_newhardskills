from django.contrib import admin

from supplier.models import Supplier, Founder


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'auto', 'reviews', 'founder')
    ordering = ('name',)
    search_fields = ('auto',)

@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'age', 'company', 'email')
    ordering = ('company',)
    search_fields = ('company',)
