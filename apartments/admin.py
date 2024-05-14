from django.contrib import admin
from  .models import Country , City,Category,Apartment,ApartmentImage,favorite
# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Apartment)
admin.site.register(ApartmentImage)
admin.site.register(favorite)
