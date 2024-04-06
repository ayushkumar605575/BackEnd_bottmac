from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products
from .serialers import *
from django.http import JsonResponse
import codecs
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(r"D:\\DJANGO\\bottmac-c81ae-firebase-adminsdk-7jwhn-46264e4462.json")
firebase_admin.initialize_app(cred)


# default_app = firebase_admin.initialize_app()

# cred = credentials.RefreshToken('path/to/refreshToken.json')
# default_app = firebase_admin.initialize_app(cred)


@api_view(["GET"])
def getData(request):
    # request.headers
    # print(request.META)
    uid = "Guest@User"
    try:
        user_auth_key = request.META.get('HTTP_AUTH')
        if user_auth_key  != "BottMac@Guest?User":
            decoded_token = auth.verify_id_token(user_auth_key, clock_skew_seconds=1)
            print(decoded_token)
            uid = decoded_token['uid']
        if uid == "Guest@User" or uid == decoded_token['uid']:
            # ProductSerializer(data=list(products), many=True).is_valid(raise_exception=True)
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
            return Response(data, status=200)
    except Exception as e:
        print(e)
        return Response([{"productId":0, "productName" :"null", "productImage" : ["",""], 'productFeatures' : "null\\nnull"}], status=200)


@api_view(["POST"])
def addProduct(request):
    print(request.data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(["POST"])
def newUser(response):
    print(response.data)
    # print("hululu",request.data)
    # if (request.method == "POST"):
    #     print("hululu",request.data)
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=200, safe=False)