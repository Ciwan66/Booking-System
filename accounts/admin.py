from django.contrib import admin
from .models import CustomUser
# Register your models here.

admin.site.register(CustomUser)
admin.site.site_title= 'Kiralleto administration'
admin.site.site_header= 'Kiralleto administration'