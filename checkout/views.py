from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.context import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your Bag is empty!')
        return redirect(reverse('services'))
    
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        "order_form": order_form,
        "stripe_public_key": 'pk_test_51HTibYKKfQej5WyLgCJK7monNBPCYZjPlh1Ct2DMnbewd12uqOEpbaBjgHOjr7ozzYJcVdNfhYcxEh47lCCE0Pho0022hS3ROM',
        "client_secret": 'test client secret',
    }

    return render(request, template, context)