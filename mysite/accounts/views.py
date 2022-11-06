from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def register(request):
   '''
      Function is used to register the user and genearte a 6 digit otp using randon module and send it on the user mail. 
   '''

def activate(request):
   '''
      Function is used to get the otp from UserOtp model and check if the otp is correct and then actiate the account by setting is_active=True. 
   '''


def login(request):
    '''
       Function is used to login in the site by .
    '''


@login_required(login_url = 'login')
def logout(request):
    '''
       Function is used to logout and for this a user need to be login
    '''

      
@login_required(login_url = 'login')
def dashboard(request):
    '''
       Function for showing the dashboard.
    '''

def my_orders(request):
    '''
       Funtion to show all the orders made.
    '''

def order_detail(request, order_id):
    '''
       Function is used to show a particular order details.
    '''


@login_required(login_url='login')
def edit_profile(request):
    '''
       Function is used to edit the profile using forms and POST method.
    '''


@login_required(login_url='login')
def change_password(request):
    '''
       Function is used to change the password using forms and POST method
    '''



