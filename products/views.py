from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Product, ProductImage, ReviewRating, AddCart, Company, CustomUser
from .forms import ReviewObject, SignUpForm, CartForm, CartPaymentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    queryset = Product.objects.all()
    mobiles = Product.objects.filter(category__name__icontains="mobile")
    tablet = Product.objects.filter(category__name__icontains="tablet")
    comp = Company.objects.all()
    return render(request, 'index.html', {'qu': queryset, 'mob': mobiles, 'tab': tablet, 'comp': comp})


# product detail
def product(request, pk):
    key = Product.objects.get(pk=pk)
    rat = ReviewRating.objects.filter(product=key)
    imag = ProductImage.objects.filter(product=key)
    if request.method == 'POST':
        form = ReviewObject(request.POST)
        if form.is_valid():
            fr = form.save(commit=False)
            fr.product = key
            fr.save()
    fm = ReviewObject(initial={})
    return render(request, 'product_detail.html', {'ke': key, 'ima': imag, 'rat': rat, 'form': fm})


# add to cart info
@login_required(login_url='/account/')
def add_to_card(request, pk):
    if request.method == 'POST':
        if not AddCart.objects.filter(product_id=pk, myuser=request.user).exists():
            AddCart.objects.create(product_id=pk, myuser=request.user)
            cartp = AddCart.objects.filter(myuser=request.user)
            total = 0.0
            shipping = 100
            for p in cartp:
                temp = (p.quantity * p.product.disc)
                total += temp
                p.price = p.product.price * p.quantity
                p.discount_price = p.product.disc * p.quantity
                p.discount = p.product.discount_off
                p.save()
            subtotal = total + shipping
            return render(request, 'checkout_cart.html', {'subtotal': subtotal, 'total': total, 'cartp': cartp})
        else:
            cartp = AddCart.objects.filter(myuser=request.user, product_id=pk)
            total = 0.0
            shipping = 100
            for p in cartp:
                q = (p.quantity + 1)
                temp = (q * p.product.disc)
                total += temp
                p.quantity = q
                p.price = p.product.price * q
                p.discount_price = p.product.disc * q
                p.discount = p.product.discount_off
                p.save()
            subtotal = total + shipping
            return render(request, 'checkout_cart.html', {'subtotal': subtotal, 'total': total, 'cartp': cartp})
    else:
        cartp = AddCart.objects.filter(myuser=request.user)
        total = 0.0
        shipping = 100
        for p in cartp:
            total += p.discount_price
        subtotal = total + shipping
        return render(request, 'checkout_cart.html', {'cartp': cartp, 'subtotal': subtotal, 'total': total})


# checkout info method
@login_required
def cart_info(request):
    if request.method == 'POST':
        current_user = request.user.id
        data = request.POST.copy()
        data.update({'myuser': current_user})
        form = CartForm(data)
        if form.is_valid():
            form.save()
            return redirect('payment_info')
    else:
        form = CartForm()
    return render(request, 'checkout_info.html', {'form': form})


# payment method
# @login_required
def payment_info(request):
    if request.method == 'POST':
        current_user = request.user.id
        data = request.POST.copy()
        data.update({'myuser': current_user})
        form = CartPaymentForm(data)
        if form.is_valid():
            cardholder_name = request.POST.get('cardholder_name')
            card_Number = request.POST.get('card_Number')
            month = request.POST.get('month')
            year = request.POST.get('year')
            csd = request.POST.get('csd')
            CustomUser.objects.update(cardholder_name=cardholder_name, card_Number=card_Number, month=month,
                                      year=year, csd=csd)
            return redirect('cart_complete')
        else:
            form = CartPaymentForm()
        return render(request, 'checkout_payment.html', {'form': form})
    return render(request, 'checkout_payment.html')


def cart_complete(request):
    return render(request, 'checkout_complete.html')


# signup method
def register(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            messages.success(request, 'Account Create Successfully !!')
            f.save()
            return HttpResponseRedirect('/account/')
    else:
        f = SignUpForm()
    return render(request, 'registeracc.html', {'form': f})


# login method
def user_login(request):
    # if not request.user.is_authenticated:
    if request.method == 'POST':
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            uname = f.cleaned_data['username']
            upass = f.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Loggged in Successfully !!')
            return HttpResponseRedirect('/')
    else:
        f = AuthenticationForm()
        return render(request, 'login.html', {'form': f})
    # else:
    #     return HttpResponseRedirect('/')


# logout method
def user_logout(request):
    logout(request)
    return redirect('/')
