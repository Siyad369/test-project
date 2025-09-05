from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.


def cart_summary(request):
    return render(request, 'cart/cart_summary.html', {})


def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        # get
        product_id = int(request.POST.get('product_id'))
        # lookup product in db
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product)

        response = JsonResponse({'Product Name': product.name})
        return response


def cart_edit(request, pk):
    return render(request, 'cart_edit.html', {})


def cart_delete(request, pk):
    return render(request, 'cart_delete.html', {})
