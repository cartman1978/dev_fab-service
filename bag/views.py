from django.shortcuts import get_object_or_404, render, redirect, reverse
from services.models import Item


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ A view to add item to the bag"""
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        
    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ A view to update quantity of the item to the specified amount"""
    
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        quantity = int(request.POST.get('item_quantity'))
        bag = request.session.get('bag', {})
        
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
            
        request.session["bag"] = bag
        return redirect(reverse("view_bag"))
        