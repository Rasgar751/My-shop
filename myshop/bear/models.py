from django.db import models
from django.urls import reverse
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара')
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Показывать?')
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'