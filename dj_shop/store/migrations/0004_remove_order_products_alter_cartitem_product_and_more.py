# Generated by Django 4.2.2 on 2023-06-23 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_order_orderitem_order_products_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='store.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
