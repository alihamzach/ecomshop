# Generated by Django 3.2 on 2022-08-30 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_addcart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcart',
            name='discount_price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addcart',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
