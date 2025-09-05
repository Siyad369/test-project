from .cart import Cart
# create context processors so our cart can work on all pages of the pages


def cart(request):
    # return the default data from out cart
    return {'cart': Cart(request)}
