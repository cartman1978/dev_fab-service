from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Item
from decimal import Decimal


def bag_contents(request):
    
    bag_items = []
    total = 0
    service_count = 0
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
    }
    
    return context