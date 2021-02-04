from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Катигория')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='Владелец продукта',)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=150, verbose_name='Имя товара')
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(verbose_name='Изобраение', null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    publication_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'
        ordering = ['-publication_date']

    @staticmethod
    def get_absolute_url():
        return '/'

    def __str__(self):
        return self.name

