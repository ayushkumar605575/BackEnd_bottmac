from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products
from .serialers import ProductSerializer
from django.http import JsonResponse
import codecs

@api_view(["GET"])
def getData(request):
    # request.headers
    try:
        products = Products.objects.all()
        print(len(products))
        data = []
        for product in products:
            id = product.productId
            name = product.productName
            features = product.productFeatures
            images = []
            for image in product.productImage:
                images.append(codecs.decode(image, 'ascii'))
            data.append({"productId":id, "productName" : name, "productImage" : images, 'productFeatures' : features})
        return JsonResponse(data, status=200, safe=False)
    except Exception as e:
        print(e.with_traceback)
        return JsonResponse({"":""}, status=200, safe=False)


@api_view(["POST"])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)