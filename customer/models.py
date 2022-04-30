from django.db import models

from customer.enums import Gender, IncomeGroup, Region


# Create your models here.


class Customer(models.Model):
    name = models.CharField(default="", max_length=128)
    gender = models.CharField(choices=Gender.choices, max_length=6, default=Gender.MALE)
    income_group = models.CharField(choices=IncomeGroup.choices, max_length=9, default=IncomeGroup.LOW)
    region = models.CharField(choices=Region.choices, max_length=5, default=Region.EAST)
    marital_status = models.BooleanField(default=False, help_text="If True means married else Unmarried")

    def __str__(self):
        return self.name
