# Generated by Django 3.1.2 on 2021-02-03 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_shop', '0004_auto_20210131_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец пользователя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=['default'], unique=True),
            preserve_default=False,
        ),
    ]
