from django.shortcuts import (render, get_object_or_404, redirect)


from .models import Item, Category
from .forms import ItemForm


def all_items(request):
    """ Get all the items page from the database.
    Handles the search queries from navigation using
    django Q object to filter the results.
    """
    
    items = Item.objects.all()
    category = None
    current_category = None
    
    if request.GET and "category" in request.GET:
        category = request.GET["category"]
        items = items.filter(category__name=category)
        current_category = get_object_or_404(Category, name=category)

    template = "services/services.html"
    
    context = {
        'item': items,
        'current_category': current_category
    }
    
    return render(request, 'services/services.html', context)


def single_item(request, item_id):
    ''' Shows the single service page '''

    item = get_object_or_404(Item, pk=item_id)


    context = {
        "item": item
    }

    return render(request, 'services/single_service.html', context)


def add_item(request):
    """ Add a item to the store """
    form = ItemForm()
    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)