from django.db import models

class SexOfPurchaser(models.TextChoices):
    Man = 'Man', 'Man'
    Woman = 'Woman', 'Woman'
