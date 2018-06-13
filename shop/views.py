from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt

from user_shop.models import UserProfiler
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views import View
from django.shortcuts import render_to_response, get_object_or_404, redirect


from shop.models import Product, Comment
from shop.forms import CommentForm
# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })
# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    recommendation = Product.objects.filter(available=True, category=product.category,price__lt =product.price ).exclude(id=product.id).order_by('?')[:4]

    return render_to_response('shop/product/detail.html',
                              {'product': product,
                               'cart_product_form': cart_product_form,
                               'recommendation': recommendation})


