from django.db import models

from core.abstract_models import  AbstractDefaultModel
from core.enums.purchaser_enums import SexOfPurchaser
from core.validators import check_phonenum


class Purchaser(AbstractDefaultModel):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')
    sex = models.CharField(
        max_length=6,
        choices=SexOfPurchaser.choices,
        default=SexOfPurchaser.Man,
        verbose_name='пол'
    )
    age = models.IntegerField(verbose_name='возраст')
    email = models.EmailField(verbose_name='почта')
    phone = models.CharField(
        max_length=13,
        validators=[check_phonenum],
        verbose_name='телефон'
    )

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.first_name

class Balance(AbstractDefaultModel):
    value = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='количество денег')
    purchasers = models.ForeignKey(
        Purchaser,
        on_delete=models.CASCADE,
        verbose_name='покупатель'
    )

    class Meta:
        ordering = ('value',)
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'

