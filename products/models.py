from django.db import models
from django.contrib.postgres.fields import ArrayField

# PRODUCTION ME "UUID" IMPLEMENT KRNA HAI

# PostgerSQL
class Products(models.Model):
    productId = models.AutoField(primary_key = True, auto_created = True)
    productName = models.CharField(max_length = 100)
    productImage = ArrayField(models.BinaryField(), default = list)
    productFeatures = models.TextField(max_length = 500)
    # productFeatures = models.TextField()

class Users(models.Model):
    # userId = models.UUIDField(unique = True, primary_key = True)
    userId = models.CharField(max_length = 100, primary_key = True)
    userName = models.CharField(max_length=60)
    userPhoneNumber = models.CharField(max_length = 13)
    userProfileUrl = models.CharField(max_length=1000)
    # userConsent = models.BooleanField()
    userCreatedAt = models.DateTimeField(auto_now = True)
    userModifiedAt = models.DateTimeField(auto_now_add = True)