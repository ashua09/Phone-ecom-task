from django.db import models
from accounts.models import Account

# Create your models here.


class Brand(models.Model):
    '''
       Model for adding different phone brands
    '''
    brand_name     = models.CharField(max_length = 100, unique = True)
    slug           = models.SlugField(max_length = 200, unique = True)
    description    = models.TextField(max_length = 300, blank = True)
    cat_image      = models.ImageField(upload_to = 'photos/categories', blank = True )

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brandes'


    def __str__(self):
        return f'{self.brand_name}'


class Phone(models.Model):
    '''
        Model for adding different phone and it's details
    '''
    phone_name  = models.CharField(max_length=100, unique=True)
    slug          = models.SlugField(max_length=200, unique=True)
    brand         = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description   = models.TextField(blank=True)
    price         = models.IntegerField()
    images        = models.ImageField(upload_to='photos/products')
    stock         = models.IntegerField()
    is_available  = models.BooleanField(default=True)
    created_date  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_name


class VariationManager(models.Manager):

    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
variation_category_choice=(
    ('color','color'),
)



class Variation(models.Model):
    '''
        Model for phone variation in phone like color
    '''
    product            = models.ForeignKey(Phone, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value    = models.CharField(max_length=100)
    is_active          = models.BooleanField(default=True)
    created_date       = models.DateTimeField(auto_now_add=True)

    
    objects = VariationManager()

    def __str__(self):
        return self.variation_value


class ReviewRating(models.Model):
    ''' 
       Model for writing phone reviews 
    '''
    product    = models.ForeignKey(Phone, on_delete=models.CASCADE)
    user       = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject    = models.CharField(max_length=100, blank=True)
    review     = models.TextField(max_length=500, blank=True)
    rating     = models.FloatField()
    ip         = models.CharField(max_length=12, blank=True)
    status     = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class ProductGallery(models.Model):
    '''
        Model for storing different images of a phone and store the images in media folder
    '''
    product = models.ForeignKey(Phone, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'phonegallery'
        verbose_name_plural = 'phone gallery'







