from django.db import models
from store.models import Phone, Variation
from accounts.models import Account

# Create your models here.


class Cart(models.Model):
    ''' 
        Model for define a cart id
    '''
    cart_id     = models.CharField(max_length=250, blank=True)
    date_added  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    
    '''
        A model containing the cart items
    '''
    user       = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product    = models.ForeignKey(Phone, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart       = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity   = models.IntegerField()
    is_active  = models.BooleanField(default=True)


    def __unicode__(self):
        return self.product