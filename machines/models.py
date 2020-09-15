from django.db import models

# Create your models here.



PRODUCT_TYPE = [
    ('Large Machine', 'Large Machine'),
    ('Small Machine', 'Small Machine'),
    ('Espresso Machine', 'Espresso Machine'),
]

CATEGORY = [
    ('Base','Base'),
    ('Premium','Premium'),
    ('Deluxe','Deluxe')
]




class CoffeeMachine(models.Model):
    product_title                   = models.CharField(max_length = 50)
    product_type                    = models.CharField(max_length = 50, choices=PRODUCT_TYPE, blank=True)
    water_line_compatible           = models.BooleanField(default=False, blank=True)
    Category                        = models.CharField(max_length = 50, choices=CATEGORY, blank=True)





    def __str__(self):
        return self.product_title



    