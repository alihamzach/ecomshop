from django.urls import path
from products import views


urlpatterns = [
    path('', views.index),
    path('<int:pk>', views.product, name="product_detail"),
    path('cart/<int:pk>', views.add_to_card, name="checkout_cart"),
    path('cartinfo/', views.cart_info, name="cart_info"),
    path('cartcomplete/', views.cart_complete, name="cart_complete"),
    path('paymentinfo/', views.payment_info, name="payment_info"),
    path('account/', views.user_login, name='account'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
