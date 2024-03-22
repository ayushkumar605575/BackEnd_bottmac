from django.db import models
import base64
from django.contrib.postgres.fields import ArrayField

# class BinaryArrayField(models.Field):
# class BinaryArrayField(models.Field):
#     def from_db_value(self, value, expression, connection):
#         if value is None:
#             return value
#         return [base64.b64decode(item.encode()) for item in value]

#     def to_python(self, value):
#         if isinstance(value, list):
#             return value
#         if value is None:
#             return value
#         return [base64.b64decode(item.encode()) for item in value.split(',')]

#     def get_prep_value(self, value):
#         if value is None:
#             return value
#         print(value)
#         return ','.join([base64.b64encode(item).decode() for item in value])

# Create your models here.
# class Products(models.Model):
#     productId = models.AutoField(primary_key = True, auto_created = True)
#     productName = models.CharField(max_length = 100)
#     productImage = ArrayField(models.BinaryField(), default = list)


# PRODUCTION ME "UUID" IMPLEMENT KRNA HAI

# PostgerSQL
class Products(models.Model):
    productId = models.AutoField(primary_key = True, auto_created = True)
    productName = models.CharField(max_length = 100)
    productImage = ArrayField(models.BinaryField(), default = list)
    productFeatures = models.TextField(max_length = 500)
    # productFeatures = models.TextField()
