from django.db import models
from apartments.models import Apartment
from django.conf import settings
# Create your models here.

class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    apartment = models.ForeignKey("apartments.apartment",on_delete=models.CASCADE)
    text = models.TextField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text
