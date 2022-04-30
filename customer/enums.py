from django.db.models import TextChoices


class Gender(TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'


class IncomeGroup(TextChoices):
    LOW = '0-$25K', '0-$25K'
    MID = '$25-$70K', '$25-$70K'
    HIGH = '>$70K', '>$70K'


class Region(TextChoices):
    EAST = 'East', 'East'
    WEST = 'West', 'West'
    NORTH = 'North', 'North'
    SOUTH = 'South', 'South'
