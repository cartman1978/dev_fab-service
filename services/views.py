from django.contrib import messages
from django.shortcuts import (render, get_object_or_404, redirect, reverse)
from django.contrib.auth.decorators import login_required

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



@login_required
def add_item(request):
    """ Add a item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only website owner can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Item successfully added!')
            return redirect(reverse('single_item', args=[item.id] ))
        else:
            messages.error(request, 'Failed to add Item. Please try again')
    else:
        form = ItemForm()
        
    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_item(request, item_id):
    """ Edit item in the store """
    if not request.use.is_superuser:
        messages.error(request, 'Sorry only website owner can do that.')
        return redirect(reverse('home'))
    
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service update successfully!')
            return redirect(reverse('single_item', args=[item.id]))
        else:
            messages.error(request, 'Failed to update service. Please try again!')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')
    
    template = 'services/edit_service.html'
    context = {
        'form': form,
        'item': item,
    }
    
    return render(request, template, context)


@login_required
def delete_item(request, item_id):
    """ Delete item from the store """
    if not request.use.is_superuser:
        messages.error(request, 'Sorry only website owner can do that.')
        return redirect(reverse('home'))
    
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('services'))