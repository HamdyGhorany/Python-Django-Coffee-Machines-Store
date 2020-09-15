from django.db import models

# Create your models here.


PRODUCT_TYPE_PODS = [
    ('Coffee Pod Large', 'Coffee Pod Large'),
    ('Coffee Pod Small', 'Coffee Pod Small'),
    ('Espresso Pod', 'Espresso Pod'),
]

COFFEE_FLAVOR = [
    ('Coffee Flavor Vanilla', 'Coffee Flavor Vanilla'),
    ('Coffee Flavor Caramel', 'Coffee Flavor Caramel'),
    ('Coffee Flavor Psl', 'Coffee Flavor Psl'),
    ('Coffee Flavor Mocha', 'Coffee Flavor Mocha'),
    ('Coffee Flavor Hazelunt', 'Coffee Flavor Hazelunt'),
]
PACKAGE_SIZE = [
    ('1 dozen (12)','1 dozen (12)'),
    ('3 dozen (36)','3 dozen (36)'),
    ('5 dozen (60)','5 dozen (60)'),
    ('7 dozen (84)','7 dozen (84)')
]

class CoffeePods(models.Model):
    pods_title                      = models.CharField(max_length = 50)
    pods_type                       = models.CharField(max_length = 50, choices=PRODUCT_TYPE_PODS, blank=True)
    coffee_flavor                   = models.CharField(max_length = 50, choices=COFFEE_FLAVOR, blank=True)
    Package_size                    = models.CharField(max_length = 50, choices=PACKAGE_SIZE, blank=True)
#    model_category                  = models.ForeignKey('Category', on_delete=models.CASCADE) # One to Many


    def __str__(self):
        return self.pods_title

#class Category(models.Model):  # Many to One
#    name = models.CharField(max_length = 25)

#    def __str__(self):
#        return self.name