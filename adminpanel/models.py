from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Banner(models.Model):
    name_Promotions = models.CharField(max_length=300)
    intro_title1 = models.CharField(max_length=400,null=True, blank=True)
    intro_title2 = models.CharField(max_length=400,null=True, blank=True)
    old_price = models.CharField(max_length=14)
    new_price = models.CharField(max_length=14)
    new_price_sub = models.CharField(max_length=14)
    image = models.ImageField(upload_to='banner_image/',null=True, blank=True)
    
    class Meta:
        verbose_name_plural =("Banner")

    def _str_(self):
        return self.name
