from django.db.models import TextChoices


class Fuel(TextChoices):
    CNG = 'CNG', 'CNG'
    PETROL = 'Petrol', 'Petrol'
    DIESEL = 'Diesel', 'Diesel'


class VehicleSegment(TextChoices):
    A = 'A', 'A'
    B = 'B', 'B'
    C = 'C', 'C'
