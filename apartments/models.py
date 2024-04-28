from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name

class Apartment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    apt_name = models.CharField(max_length=255)
    description = models.TextField()
    district = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)
    rooms = models.IntegerField()
    beds = models.IntegerField()
    bath_rooms = models.IntegerField()
    wifi = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.apt_name

