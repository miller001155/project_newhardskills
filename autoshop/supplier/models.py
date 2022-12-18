from django.db import models
from django_countries.fields import CountryField

from core.validators import check_age


# поставщик, основатель
class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    location = CountryField()
    email = models.EmailField()
    auto = models.CharField(max_length=255, verbose_name='Авто')
    reviews = models.TextField(max_length=500, verbose_name='Отзывы')
    founder = models.ForeignKey(
        'Founder',
        on_delete=models.CASCADE
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name

class Founder(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.SmallIntegerField(validators=[check_age], verbose_name='Возраст')
    company = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.first_name