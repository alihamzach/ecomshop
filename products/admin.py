from django.contrib import admin
from .models import Product, Category, Company, ProductImage, ReviewRating, AddCart, CustomUser
# Register your models here.


class ProductDetail(admin.ModelAdmin):
    list_display = ['id', 'p_name']


admin.site.register(Product, ProductDetail)


class CategoryDetail(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Category, CategoryDetail)


class CompanyDetail(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Company, CompanyDetail)


class ProductImageDetail(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(ProductImage, ProductImageDetail)


class ReviewRatingDetail(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'review']


admin.site.register(ReviewRating, ReviewRatingDetail)


class CartDetail(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'discount', 'price', 'discount_price']


admin.site.register(AddCart, CartDetail)


class CustomUserDetail(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'company_name', 'area_code',
                    'primary_phone', 'street_address', 'zip_code', 'busniess_address']


admin.site.register(CustomUser, CustomUserDetail)


