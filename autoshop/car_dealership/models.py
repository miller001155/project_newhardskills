from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModel
from core.enums.car_dealership_enums import Currency, StatusOfCar
from core.validators import check_raiting


class Car(AbstractDefaultModel):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    year = models.SmallIntegerField(verbose_name='Год', default=1995)
    price = models.IntegerField(default=10000, verbose_name='Цена')
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD,
        verbose_name='валюта'
    )
    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    status = models.CharField(
        max_length=255,
        choices=StatusOfCar.choices,
        default=StatusOfCar.Available,
        verbose_name='статус'
    )
    class Meta:
        ordering = ('title',)
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.title

class Category(AbstractDefaultModel):
    name = models.CharField(max_length=255, verbose_name='категория')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name

class Raiting(AbstractDefaultModel):
    value = models.IntegerField(validators=[check_raiting], default=1, verbose_name='рейтинг')
    cars = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='raiting'
    )

    class Meta:
        ordering = ('value',)
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'



class Car_dealership(AbstractDefaultModel):
    name = models.CharField(max_length=255, verbose_name='имя')
    characteristic = models.TextField(blank=True, verbose_name='характеристика')
    location = CountryField(verbose_name='локация')
    contact = models.EmailField(verbose_name='почта')
    cars = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Автосалон'
        verbose_name_plural = 'Автосалоны'

    def __str__(self):
        return self.name

