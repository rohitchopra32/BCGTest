from django.db import models

from customer.models import Customer
from policy.enums import Fuel, VehicleSegment


class Policy(models.Model):
    fuel = models.CharField(choices=Fuel.choices, max_length=6, default=Fuel.CNG)
    vehicle_segment = models.CharField(choices=VehicleSegment.choices, max_length=1, default=VehicleSegment.A)
    premium = models.PositiveIntegerField()
    bodily_injury_liability = models.BooleanField(default=False)
    personal_injury_protection = models.BooleanField(default=False)
    property_damage_liability = models.BooleanField(default=False)
    collision = models.BooleanField(default=False)
    comprehensive = models.BooleanField(default=False)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.pk}"


class CustomerPolicies(models.Model):
    policy = models.ForeignKey(Policy, related_name='customer_policy', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name="policies", on_delete=models.CASCADE)
    date_of_purchase = models.DateField()

    def __str__(self):
        return f"{self.customer.name} - {self.policy_id}"
