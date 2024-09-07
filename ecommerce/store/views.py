from django.shortcuts import render
from .models import PcPart, Specs, Review, Order, OrderItem, ShippingAddress

# Create your views here.
def store(request):
    template_name = 'store/store.html'
    parts = PcPart.objects.all()

    context = {
        'parts' : parts
    }
    return render(request, template_name, context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.items.all()  # Retrieve related OrderItem objects
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items' : 0}

    template_name = 'store/cart.html'

    context = {
        'items': items,
        'order': order,
    }
    return render(request, template_name, context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.items.all()  # Retrieve related OrderItem objects
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items' : 0}

    template_name = 'store/checkout.html'

    context = {
        'items': items,
        'order': order,
    }


    return render(request, template_name, context)



