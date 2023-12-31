# Generated by Django 3.2 on 2022-09-01 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_myuser_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='card_Number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='cardholder_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='csd',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
