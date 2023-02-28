from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    postal_code = models.IntegerField()


class BeerType(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)


class Beer(models.Model):
    BITTER = 'BT'
    SWEET = 'SW'
    SOUR = 'SO'
    BITTER_SOUR = 'BT-SO'
    BITTER_SWEET = 'BT-SW'
    SWEET_SOUR = 'SW-SO'
    NO_AROMA = 'No aroma'
    aroma_choice = [
        (BITTER, 'Bitter'),
        (SWEET, 'Sweet'),
        (SOUR, 'Sour'),
        (BITTER_SOUR, 'Bitter-Sour'),
        (BITTER_SWEET, 'Bitter-Sweet'),
        (SWEET_SOUR, 'Sweer-Sour'),
        (NO_AROMA, 'No aroma')
    ]

    beer_type = models.ForeignKey('BeerType', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    alcohol_percentage = models.DecimalField(max_digits=2, decimal_places=1)
    color = models.CharField(max_length=255)
    aroma_choice = models.CharField(max_length=255, choices=aroma_choice)
    water_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    barley_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    hop_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    yeast_percentage = models.DecimalField(max_digits=4, decimal_places=2)


class Review(models.Model):

    grade = models.IntegerField()
    beer = models.ForeignKey('Beer', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(max_length=50)
