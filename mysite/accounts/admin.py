from django.contrib import admin
from .models import Account,UserProfile,UserOTP

# Register your models here.

admin.site.register(Account)
admin.site.register(UserOTP)
admin.site.register(UserProfile)