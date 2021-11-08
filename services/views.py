from django.shortcuts import render
from .models import Item


def all_items(request):
    """ Get all the items page from the database.
    Handles the search queries from navigation using
    django Q object to filter the results.
    """
    
    items = Item.objects.all()
    
    context = {
        'item': items
    }
    
    return render(request, 'services/services.html', context)
