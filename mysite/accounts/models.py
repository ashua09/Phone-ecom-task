from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    '''
       Custom user model manager where email and username is must
       and unique for authentication
    '''

    def create_user(self , first_name, last_name, username, email, password=None):
        '''
           Model to create and save the user with given email and password
        '''
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email      = self.normalize_email(email),
            username   = username,
            first_name = first_name,
            last_name  = last_name,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self , first_name, last_name, username, email, password):

        '''
           Model to create and save the superuser with given email and password
        '''
        user = self.create_user(
            email      = self.normalize_email(email),
            username   = username,
            password   = password,
            first_name = first_name,
            last_name  = last_name,

        )
        user.is_admin      = True
        user.is_active     = True
        user.is_staff      = True
        user.is_superadmin = True

        user.save(using=self.db)
        return user

class Account(AbstractUser):

    '''
       Models for user auth in admin panel 
    '''

    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)
    username      = models.CharField(max_length=100, unique=True)
    email         = models.EmailField(max_length=100, unique=True)
    phone_number  = models.CharField(max_length=50)

    #login_field
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()


    def __str__(self):
        return self.email
    

class UserProfile(models.Model):
    '''
       Model for user profile 
    '''
    user            = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1  = models.CharField(blank=True, max_length=100)
    address_line_2  = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='userprofile')
    city            = models.CharField(blank=True, max_length=20)
    state           = models.CharField(blank=True, max_length=20)
    country         = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name

    
class UserOTP(models.Model):
    '''
       Used to save the otp 
    '''
    
    user         = models.ForeignKey(Account, on_delete=models.CASCADE)
    otp          = models.SmallIntegerField()
    created_at   = models.DateTimeField(auto_now=True)
    