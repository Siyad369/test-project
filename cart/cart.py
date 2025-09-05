class Cart:
    def __init__(self, request):
        self.session = request.session

        # get the current session if it exists
        cart = self.session.get('session_key')

        # if the user is new, no session key, create one

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart is availabe on all pages of site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __iter__(self):
        """
        This makes the Cart object iterable, so you can do:
        {% for item in cart %}
        """
        for product_id, item in self.cart.items():
            yield {
                'product_id': product_id,
                'price': item['price']
            }

    def __len__(self):
        """
        Optional: allows using len(cart) in templates
        """
        return len(self.cart)