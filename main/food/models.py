from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=500, default='https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_500,h_376,al_c,lg_1,q_80,enc_auto/food-placeholder.jpg')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

