from django.shortcuts import render

# Create your views here.

def place_order(request):
    '''
       Function first check if cart is empty or not, if not then place the order
       and add all the billing information inside the order table
       then generate the order number then go to checkout page.
    '''   


def payments(request):
    '''
       Function is used make the transaction and save it into the payment model
       and send the confirmation mail to user.
    '''


def order_complete(request):
    '''
       This Function render a page where all the details of the placed order is shown.
    '''













