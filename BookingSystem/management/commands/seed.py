from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from apartments.models import Country, City, Category, Apartment, ApartmentImage
import random

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Örnek ülkeler oluştur
        countries = []
        for _ in range(5):
            country = Country.objects.create(country_name=fake.country())
            countries.append(country)

        # Örnek şehirler oluştur
        cities = []
        for _ in range(10):
            city = City.objects.create(city_name=fake.city(), postal_code=fake.postcode(), country=random.choice(countries))
            cities.append(city)

        
        # Örnek apartmanlar oluştur
        for _ in range(20):
            apartment = Apartment.objects.create(
                category=random.choice(categories),
                country=random.choice(countries),
                city=random.choice(cities),
                actual_address=fake.address(),
                maps_link=fake.uri(),
                apt_name=fake.company(),
                description=fake.text(),
                district=fake.city_suffix(),
                is_active=random.choice([True, False]),
                is_booked=random.choice([True, False]),
                rooms=random.randint(1, 5),
                beds=random.randint(1, 10),
                bath_rooms=random.randint(1, 5),
                wifi=random.choice([True, False]),
                tv=random.choice([True, False]),
                price_per_night=random.randint(50, 200),
                user=User.objects.first()  # İsterseniz burada bir kullanıcı ata
            )
            
            # Örnek apartman resimleri oluştur
            for _ in range(random.randint(1, 5)):
                ApartmentImage.objects.create(apartment=apartment, image=fake.image_url())

            
        self.stdout.write(self.style.SUCCESS('Sample data populated successfully'))
