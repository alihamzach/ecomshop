from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    trending = models.BooleanField(default=False)
    image = models.ImageField(upload_to='abc')
    discount_off = models.IntegerField()
    p_name = models.CharField(max_length=50)
    spec = models.CharField(max_length=50)
    descp = models.CharField(max_length=100)
    price = models.IntegerField()
    disc = models.IntegerField()
    size = models.CharField(max_length=700)
    weight = models.CharField(max_length=50)
    os = models.CharField(max_length=500)
    resolution = models.CharField(max_length=500)
    memory = models.CharField(max_length=100)

    def __str__(self):
        return self.p_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="abc")


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    review = models.TextField(max_length=700)

    def __str__(self):
        return self.name


class AddCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    myuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discount_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.p_name


class CustomUser(models.Model):
    myuser = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    company_name = models.CharField(max_length=70, null=True, blank=True)
    area_code = models.CharField(max_length=20)
    primary_phone = models.CharField(max_length=20)
    street_address = models.CharField(max_length=70)
    zip_code = models.CharField(max_length=30)
    busniess_address = models.BooleanField(default=False)
    cardholder_name = models.CharField(max_length=50, null=True)
    card_Number = models.CharField(max_length=30, null=True)
    month = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    csd = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name
