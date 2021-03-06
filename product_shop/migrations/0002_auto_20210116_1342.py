# Generated by Django 3.1.2 on 2021-01-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-publication_date'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изобраение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
