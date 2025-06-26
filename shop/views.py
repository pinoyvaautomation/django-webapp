#from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render

# Create your views here.

# shop/views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Order, OrderItem
from .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Additional views for cart, checkout, etc.

# shop/views.py (example for adding to cart)
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Get quantity from form input
    cart = request.session.get('cart', {})
    '''
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')'''
    # Update quantity: add the new quantity to the existing quantity
    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity

    request.session['cart'] = cart  # Save updated cart in the session
    return redirect('cart_detail')

# Add to cart view that display all cart added.
def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity,
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart_detail.html', context)

# will loop through the quantities submitted in the form and update the cart session accordingly.
def update_cart(request):
    cart = request.session.get('cart', {})

    # Loop through the POST data and update cart quantities
    for product_id, quantity in request.POST.items():
        if product_id.startswith("quantity_"):
            actual_product_id = product_id.split("quantity_")[1]
            try:
                quantity = int(quantity)
                if quantity > 0:
                    cart[actual_product_id] = quantity  # Update quantity
                else:
                    cart.pop(actual_product_id)  # Remove if quantity is zero
            except ValueError:
                continue  # Ignore invalid quantity values

    request.session['cart'] = cart  # Save updated cart in the session
    return redirect('cart_detail')


#  create a view that displays the order form, saves the data, and creates an order.
def order_request(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')  # Redirect if cart is empty

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()

            # Add items to the order
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            # Clear cart after order submission
            request.session['cart'] = {}
            return redirect('order_confirmation')
    else:
        form = OrderForm()

    return render(request, 'order_request.html', {'form': form})


# After the form is submitted, redirect users to an order confirmation page.
# shop/views.py
def order_confirmation(request):
    return render(request, 'order_confirmation.html')

