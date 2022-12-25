from django.contrib import admin

from purchaser.models import *


@admin.register(Purchaser)
class PurchaserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'age', 'email', 'phone')
    ordering = ('second_name',)
    search_fields = ('second_name',)


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('purchasers','value')
    ordering = ('value',)
    search_fields = ('purchaser',)
