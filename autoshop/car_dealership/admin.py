from django.contrib import admin

from car_dealership.models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'currency', 'cat')
    ordering = ('title',)
    search_fields = ('title__istarwith',)


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

