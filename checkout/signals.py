from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_total_on_save(sender, instance, created, **kwargs):
    ''' update total when lineitem is created or updated '''

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_total_on_delete(sender, instance, **kwargs):
    ''' Update total when a lineitem is deleted '''

    instance.order.update_grand_total()