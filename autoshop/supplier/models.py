from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModel
from core.validators import check_age


# поставщик, основатель
class Supplier(AbstractDefaultModel):
    name = models.CharField(max_length=255, verbose_name='Имя')
    location = CountryField(verbose_name='Страна')
    email = models.EmailField(verbose_name='почта')
    auto = models.CharField(max_length=255, verbose_name='Авто')
    reviews = models.TextField(max_length=500, verbose_name='Отзывы')
    founder = models.ForeignKey(
        'Founder',
        on_delete=models.CASCADE,
        verbose_name='основатель'
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name

class Founder(AbstractDefaultModel):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.SmallIntegerField(validators=[check_age], verbose_name='Возраст')
    company = models.CharField(max_length=255, verbose_name='Компания')
    email = models.EmailField(verbose_name='почта')

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.first_name