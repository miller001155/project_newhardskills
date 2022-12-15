from django.contrib import admin

from purchaser.models import Balance, Purchaser


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('value', 'purchaser')
    ordering = ('-purchaser',)
    search_fields = ('value',)


@admin.register(Purchaser)
class PurchaserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'sex', 'phone')
    ordering = ('-first_name',)
    search_fields = ('first_name',)
