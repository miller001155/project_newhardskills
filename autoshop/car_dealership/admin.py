from django.contrib import admin, messages
from django.db.models import QuerySet

from car_dealership.models import *
from core.enums.car_dealership_enums import Currency

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'currency', 'cat')
    ordering = ('title',)
    search_fields = ('title__istartwith',)
    actions = ('change_to_euro',)

    @admin.action(description='Изменить валюту на евро')
    def change_to_euro(self, request, qs: QuerySet):
        updates_cars = qs.update(currency=Currency.EUR)
        self.message_user(
            request,
            f'Обновлено {updates_cars} записей',
            messages.SUCCESS
        )


@admin.register(Car_dealership)
class Car_dealershipAdmin(admin.ModelAdmin):
    list_display = ('location', 'name')
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ('value', 'cars')
    ordering = ('value',)
    search_fields = ('value',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

