from django.shortcuts import render

# Create your views here.
def _cart_id(request):  
    '''
    Generating a cart id using session key
    '''

def add_cart(request):

    '''
        Function to add the item in the cart.
        Check if the user is authenticated and then add item , 
        if the item is already in the cart than increase the quantity. 
    '''

def remove_cart(request):

    '''
       First check the user is authenticated and then if their is some item in cart,
       then decrease the quantity of item in cart by 1

    '''
def delete_cart(request):
    
    '''
       First check the user is authenticated and then if their is some item in cart,
       then empty the cart, delete all itmes

    '''

def cart(request):
    
    '''
       Function to calculate the total item and the total amount
       and then passed in the context dictionary and load it on template
    '''

def checkout(request):

    '''
       First check if user is authenticated then get all the cart item and total amount and render it 
       on the chekout page
    '''