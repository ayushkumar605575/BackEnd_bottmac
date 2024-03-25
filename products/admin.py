from django.contrib import admin
from .models import UserAccount, Products
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Products)
admin.site.register(UserAccount)