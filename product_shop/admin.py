from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'image', 'description', 'publication_date')
    list_display_links = ('name', 'price', 'description')
    search_fields = ('name', 'price', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
