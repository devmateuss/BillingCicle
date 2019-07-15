from django.core.validators import MinValueValidator
from django.db import models

STATUS_DEBIT_CHOICES = [
    (1, 'PAID_OUT'),
    (0, 'PENDING'),
    (2, 'SCHEDULED'),
]


class Credit(models.Model):
    name = models.CharField(max_length=255, null=False)
    value = models.IntegerField(validators=[MinValueValidator(0, message='O valor minimo deve ser 0')], null=False)


class Debit(models.Model):
    name = models.CharField(max_length=255, null=False)
    value = models.IntegerField(validators=[MinValueValidator(0, message='O valor minimo deve ser 0')], null=False)
    status = models.CharField(max_length=10 ,choices=STATUS_DEBIT_CHOICES, default=STATUS_DEBIT_CHOICES[1], null=False)


class BillingCicle(models.Model):
    name = models.CharField(max_length=255, null=False)
    month = models.IntegerField(validators=[MinValueValidator(1, message='O valor minimo deve ser 1'),
                                         MinValueValidator(12, message='O valor maximo deve ser 12')],
                             null=False
                             )
    year = models.IntegerField(validators=[MinValueValidator(1970, message='O valor minimo deve ser 1970'),
                                         MinValueValidator(2200, message='O valor maximo deve ser 2200')],
                                null=False
                                )
    credits = models.ManyToManyField(Credit)
    debits = models.ManyToManyField(Debit)