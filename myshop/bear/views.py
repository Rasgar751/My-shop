from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Product, Profile
from .forms import UserRegistrationForm, LoginForm
from cart.forms import CartAddProductForm

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'bear/product/list.html', {'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'bear/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'bear/registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'bear/registration/register.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Неверный аккаунт')
            else:
                return HttpResponse('Недействительный логин')
    else:
        form = LoginForm()
    return render(request, 'bear/registration/login.html', {'form': form})

