from django.db import models


class Category(models.Model):
    """ Model for service categories"""
    
    class Meta:
        """ override default s onto the end of the model name"""
        verbose_name_plural = "Categories"
    
    name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150,
                                    null=True,
                                    blank=True)

    def __str__(self):
        """ Override default object name"""
        
        return self.name
    
    def get_display_name(self):
        """ Function to return display name"""
        
        return self.display_name

    
class Item(models.Model):
    code = models.CharField(max_length=150,
                            null=True,
                            blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey("Category",
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name