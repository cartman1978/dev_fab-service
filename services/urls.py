from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='services'),
    path("<int:item_id>/", views.single_item, name="single_item"),
    
]