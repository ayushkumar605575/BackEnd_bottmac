from django.shortcuts import render, redirect
# from .forms import ImageUploadForm
from .models import Products#, ImageModel
from base64 import b64encode, b64decode
from io import BytesIO
import codecs
from .user_serialer import UserSerializer
def user_creation(request):
    if request.method == "POST":
        newUser = UserSerializer(request.data)
        if newUser.is_valid():
            newUser.save()
        return #SomeThing


def compress_image(image):
    file_content = image.read()
    
    # Convert the content to bytes
    bytes_content = BytesIO(file_content).read()
    
    return bytes_content

def handle_uploaded_file(f, i):
    with open(f"tmp{i}.jpeg", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_image(request):
    if request.method == 'POST':
        print()
        if request.FILES and len(request.POST.get("features")) != 0 and len(request.POST.get('name')) != 0:
            productName = request.POST.get('name')
            productImages = request.FILES.getlist('images')
            productFeatures = request.POST.get("features")
            print(productFeatures)

            image_bytes = []
            for productImage in productImages:
                # print(productImage)
                # print(b''.join(list(productImage.chunks())))
                image_bytes.append(b64encode(b''.join(list(productImage.chunks()))))
            # print(image_bytes)
        
            product_model = Products()
            # image_model.productId = 1
            product_model.productName = productName
            # if image_model.productImage:
            product_model.productImage.extend(image_bytes)
            product_model.productFeatures = productFeatures
            product_model.save()
            return redirect('image_display')
    return render(request, 'upload.html')

def display_image(request):
    product_model = Products.objects.last()  # Retrieve the last uploaded image
    print(product_model)
    if product_model:
        # print(len(image_model.productImage))
        name = product_model.productName
        print(name)
        images = []
        for image in product_model.productImage:
            images.append(codecs.decode(image, 'ascii'))
        # print(len(images))
        # print(images[0])
        print(product_model.productFeatures)
        features = product_model.productFeatures.split("\\n")
        return render(request, 'display.html', {'image_model': images, 'name':name, 'features':features})
    return render(request, 'display.html', {'image_model':"No Image Available",'name': ""})
