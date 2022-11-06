from django.shortcuts import render


# Create your views here.
def home(request, category_slug=None):
    
    '''
       Home page for the site where all the product and category are shown
       Here can use the paginator to load limited amount of phone and also
       the total phones available and render it on a template
    
    '''

def phone_detail(request, brand_slug, phone_slug):


    '''
        Getting the detail of the single product and all the reviews for the product adn also the average review
        and then use the context dictionary to render the info. on the particular template.
        In this we use the brand slug and phone slug to get that product

    '''


def search(request):

    '''
       This function is used to make the active search bar where a user can search for the product
    
    '''

def submit_review(request, phone_id):
    
    ''' 
        
        This function is for submitting the reviews.
         
        Here first checking if the review is already made then update the review 
        and if not then make a new review .
       
    
    '''
