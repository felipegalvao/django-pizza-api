from django.db import models

class Pizza(models.Model):
    SIZE_30 = '30'
    SIZE_50 = '50'
    PIZZA_SIZES = (
        (SIZE_30, '30 cm'),
        (SIZE_50, '50 cm'),
    )

    size = models.CharField(
        max_length=2,
        choices=PIZZA_SIZES,
    )
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=200)
