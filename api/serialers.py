from rest_framework import serializers
from products.models import Products, UserAccount

class ProductSerializer(serializers.ModelSerializer):
    # productImages = serializers.ListSerializer(child  = Products.productImage)
    # productImages = serializers.SerializerMethodField("get_productImage")#.ListSerializer(child = serializers.CharField())
    class Meta:
        model = Products
        fields = "__all__" #["productId", "productName", "productFeatures"]

    # print(productImage)

    # def validate_productImage(self, value):
        # print(value,"dsfkuhrf")
    # Implement validation logic here based on your image storage approach
    # For example, check if URLs are valid or Base64 strings are properly formatted
        # for _ in value:
        # Add your specific validation logic here
            # pass
    #     # return value
    # def get_productImage(self, obj):
    # # # Assuming productImage stores Base64 encoded image data
    #     print(type(obj))
    #     if obj.productImage:
    #         print(obj.productImage)
    #         return list(obj.productImage)  # Assuming only one image per product for now
    #     return None
    # def productImage(self, product):
        # print(product)
        # return list(product.productImages)

# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'