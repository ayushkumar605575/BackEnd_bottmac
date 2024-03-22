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
